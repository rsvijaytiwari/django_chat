from django.urls import path

from authentication.views import account_authenticate

urlpatterns = [
    path("v1/account/authenticate", account_authenticate)
]