# Import serializer tools from Django REST Framework
from rest_framework import serializers
#password hashing utility which converts plain text to secured 
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib.auth import authenticate

#create serializer class for user model
#model serializer automatically creates fields 
class UserSerializer(serializers.ModelSerializer): 

    class Meta:
        model = User
        fields = ['username','email','password','contactnumber', 'role']
        extra_kwargs = {
            'password': {'write_only': True} #Accept password when creating/updating user, but never include it in API response.
        }

    def create(self, validated_data): #self instance of serializer
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data) #** unpack the dictionary      



class LoginSerializer(serializers.Serializer): #serializer for login endpoint
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
                
        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError({
                "detail": "Invalid username or password."
            })

        if  user.role != "USER":
            raise serializers.ValidationError({
                "detail": "Access denied for admin users."
            })
                       
        data['user'] = user
        return data        
            
        