from django.contrib import admin

from connect.models import Connect


@admin.register(Connect)
class ConnectAdmin(admin.ModelAdmin):
    list_display = ["from_user", "to_user", "is_connected", "modified_at", "created_at"]
