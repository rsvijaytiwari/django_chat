from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, null=True)
    uuid = models.UUIDField(null=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True, unique=True, null=True)
    alternate_email = models.EmailField(blank=True, unique=True, null=True)
    alternate_phone_number = PhoneNumberField(blank=True, unique=True, null=True)
    two_step_verification = models.BooleanField(default=False)
    extended_type = models.CharField(max_length=50, choices=(
        ("A", "Administrator"),
        ("C", "Customer"),
        ("M", "Management"),
        ("D", "Debugger")
    ), default="A")
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_phone_number_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{str(self.date_joined.date()).replace('-', '')}{str(self.id)}"

    class Meta:
        verbose_name_plural = "Users"
