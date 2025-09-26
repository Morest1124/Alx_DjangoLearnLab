from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """A serializer for the book model.
    
    automatically handles serializations for all fields as set field = '__all__'
    """
    class Meta:
        #book model
        model = Book
        
        #Include all fields
        field = '__all__'
        
        
    