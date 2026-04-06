from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout


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


# @api_view(['POST'])
# def login_user(request):
#     serializer = LoginSerializer(data=request.data)

#     if serializer.is_valid():
#         user = serializer.validated_data['user']

#         refresh = RefreshToken.for_user(user)

#         return Response(
#             {
#                 "access_token": str(refresh.access_token),
#                 "refresh_token": str(refresh)
#             },
#             status=status.HTTP_200_OK
#         )

#     return Response(
#         {
#             "message": "Login failed",
#             "errors": serializer.errors
#         },
#         status=status.HTTP_400_BAD_REQUEST
#     )

@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

    is_json = request.content_type == 'application/json'

    data = request.data if is_json else request.POST
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        user = serializer.validated_data['user']

        login(request, user)

        refresh = RefreshToken.for_user(user)

        if is_json:
            return Response(
                {
                    "access_token": str(refresh.access_token),
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "role": user.role
                    },                    
                    
                    "refresh_token": str(refresh)
                },
                status=status.HTTP_200_OK
            )

        return redirect('user_dashboard')

    if is_json:
        return Response(
            {
                "message": "Login failed",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return render(
        request,
        'user/login.html',
        {"errors": serializer.errors}
    )


@api_view(['POST'])
def user_logout(request):

    try:
        is_json = request.content_type and 'application/json' in request.content_type

        refresh_token = (
            request.data.get("refresh_token")
            if is_json else request.POST.get("refresh_token")
        )

        logout(request)

        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()

        if is_json:
            return Response(
                {"message": "Logout successful"},
                status=status.HTTP_200_OK
            )

        return redirect('login_user')

    except Exception as e:
        if 'application/json' in request.content_type:
            return Response(
                {"message": "Logout failed", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return redirect('login_user')


@login_required
def user_dashboard(request):
    return render(request, 'user/dashboard.html')
