from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token 

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing and updating user profile information.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture')
        read_only_fields = ('username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user account (registration).
    """
    # The password field is write-only for security
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        # Use the custom model's create_user method to ensure the password is hashed
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        
        # Optional: Automatically create an authentication token for the new user
        Token.objects.create(user=user) 
        
        return user