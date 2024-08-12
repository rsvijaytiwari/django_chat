from django.contrib.auth.hashers import check_password
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User


@api_view(["POST"])
@permission_classes([AllowAny])
def account_authenticate(request):
    d = request.data
    if "email" in d:
        user_qs = User.objects.filter(email=d["email"])
        if user_qs.exists():
            user_get = user_qs.get()
            if check_password(d["password"], user_get.password):
                refresh = RefreshToken.for_user(user_qs.get())
                return Response({
                    "uuid": user_get.uuid,
                    "credentials": {
                        "auth": {
                            "refresh": str(refresh),
                            "access": str(refresh.access_token)
                        },
                    }
                }, status=200)
            return Response({
                "status": "wrong_password",
                "reason": "wrong password try again"
            }, status=400)
        else:
            return Response({
                "status": "no_user_found",
                "reason": "no user account found"
            }, status=400)
    return Response({
        "status": "invalid_request",
        "reason": "user credential are missing"
    }, status=400)
