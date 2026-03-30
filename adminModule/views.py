from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view, permission_classes
from productModule.permissions import IsAdminUserRole
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import UserSerializer

@api_view(['POST'])
def admin_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)

    if user.role != 'ADMIN':
        return Response({"error": "Only admin can login here"}, status=403)

    refresh = RefreshToken.for_user(user)

    return Response({
        "access_token": str(refresh.access_token),
    })
    
    
@api_view(['GET'])
@permission_classes([IsAdminUserRole])
def viewUsers(request):
    User = get_user_model()  # return active user model
    print(User, "User")
    users = User.objects.exclude(role='ADMIN')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
