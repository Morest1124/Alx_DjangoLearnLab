from rest_framework import serializers
from django.contrib.auth import get_user_model 
from rest_framework.authtoken.models import Token 

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing and updating user profile information.
    This serializer is used for authenticated user profiles.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture')
    
        read_only_fields = ('username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user account (registration).
    """
    # Define the password field as write-only and required
    
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        # Ensure password is only used for creation/update, not reading
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        
        # Automatically create an authentication token for the new user
        Token.objects.create(user=user) 
        
        return user
