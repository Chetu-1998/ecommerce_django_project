from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response(
            {
                "message": "User registered successfully",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                }
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        {
            "message": "Registration failed",
            "errors": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            },
            status=status.HTTP_200_OK
        )

    return Response(
        {
            "message": "Login failed",
            "errors": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    try:
        # get refresh token from request body
        refresh_token = request.data["refresh_token"]

        if not refresh_token:
            return Response(
                {"message": "Refresh token is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response(
            {"message": "Logout successful"},
            status=status.HTTP_205_RESET_CONTENT
        )

    except Exception as e:
        return Response(
            {"message": "Logout failed", "error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
