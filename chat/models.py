from django.db import models


class Chat(models.Model):
    connection_reference = models.ForeignKey(
        "connect.Connect", on_delete=models.CASCADE
    )
    from_user = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, related_name="chat_from_user", null=True
    )
    to_user = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, related_name="chat_to_user", null=True
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
