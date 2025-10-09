from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Import your custom user model and serializer
from .models import CustomUser 
from .serializers import CustomUserSerializer 

# Create your views here.
