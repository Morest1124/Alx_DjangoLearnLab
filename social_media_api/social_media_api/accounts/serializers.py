from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    """ Serializer for users"""
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ['id']
        
