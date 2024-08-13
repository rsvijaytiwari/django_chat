import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Q

from authentication.models import User
from chat.models import Chat
from connect.models import Connect


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.room_group_name = None
        self.room_name = None

    async def connect(self):
        self.user = self.scope['user']
        self.room_name = f"user_{self.user.id}"
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            message = data.get('message')
            to_user_id = data.get('to_user_id')

            from_user = self.user

            # Check if the connection exists between from_user and to_user in either direction
            is_connected, connection = await self.is_user_connected(from_user.id, to_user_id)

            if not is_connected:
                await self.send(text_data=json.dumps({
                    'error': 'You are not connected to this user.'
                }))
                return

            # Save the message to the database
            chat = await self.save_chat_message(from_user.id, to_user_id, connection, message)

            broadcast_data = {
                'message': message,
                'from_user_id': from_user.id,
                'to_user_id': to_user_id,
                'timestamp': str(chat.created_at)
            }

            await self.channel_layer.group_send(
                f"chat_user_{to_user_id}",
                {
                    'type': 'chat_message',
                    'message': broadcast_data
                }
            )

            await self.send(text_data=json.dumps({
                'success': 'Message sent successfully.'
            }))

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def is_user_connected(self, from_user_id, to_user_id):
        try:
            from_user = User.objects.get(id=from_user_id)
            to_user = User.objects.get(id=to_user_id)

            # Check for a connection in either direction
            connection = Connect.objects.filter(
                (Q(from_user=from_user) & Q(to_user=to_user)) |
                (Q(from_user=to_user) & Q(to_user=from_user)),
                is_connected=True
            ).first()

            if connection:
                return True, connection
            return False, None
        except User.DoesNotExist:
            return False, None

    @database_sync_to_async
    def save_chat_message(self, from_user_id, to_user_id, connection, message):
        from_user = User.objects.get(id=from_user_id)
        to_user = User.objects.get(id=to_user_id)

        chat = Chat.objects.create(
            connection_reference=connection,
            from_user=from_user,
            to_user=to_user,
            message=message
        )
        return chat