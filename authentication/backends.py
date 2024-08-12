from asyncio.log import logger

import jwt
from channels.db import database_sync_to_async
from django.conf import settings
from django.db import close_old_connections

from authentication.models import User


class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        close_old_connections()

        token = None

        # Extract token directly from the Authorization header (no Bearer prefix)
        for header in scope['headers']:
            if header[0] == b'authorization':
                token = header[1].decode()
                break

        if token is None:
            logger.info("No JWT token found; rejecting connection.")
            await self._send_error(send, "No JWT token found.")
            return

        try:
            # Decode the JWT token
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_data.get('user_id')

            # Fetch the user from the database
            user = await database_sync_to_async(User.objects.get)(id=user_id)
            scope['user'] = user
            logger.info(f"Authenticated user: {user}")

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist) as e:
            logger.warning(f"Authentication failed: {e}")
            await self._send_error(send, "Invalid or expired JWT token.")
            return

        # Pass control to the next middleware or consumer
        return await self.app(scope, receive, send)

    async def _send_error(self, send, message):
        """
        Send an error message to the WebSocket and close the connection.
        """
        await send({
            'type': 'websocket.close'
        })
        logger.info(f"WebSocket connection closed: {message}")
