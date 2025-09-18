from rest_framework import generics
from .serializers import BookSerializer
from django.urls import path
from .models import Book

# Create your views here.
class BookList(generics.ListAPIView):
    """API view listing all books
    
    provide a readonly endpoint"""
    #set all queryset of all objects to be retrived
    queryset = Book.objects.all()
    
    serializer_class =BookSerializer # tells how to serialize