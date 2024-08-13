from django.db import models


class Connect(models.Model):
    from_user = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, related_name="from_user"
    )
    to_user = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, related_name="to_user"
    )
    is_connected = models.BooleanField(default=False)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
