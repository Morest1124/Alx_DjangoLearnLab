from rest_framework import generics
from .serializers import BookSerializer
from django.urls import path
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer


# Create your views here.
class BookList(generics.ListAPIView):
    """API view listing all books
    
    provide a readonly endpoint"""
    #set all queryset of all objects to be retrived
    queryset = Book.objects.all()
    
    serializer_class =BookSerializer # tells how to serialize
    
   

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.

    This ViewSet automatically provides actions for the Book model.
    """
    # The queryset defines the set of objects that this ViewSet will operate on.
    queryset = Book.objects.all()
    
    # The serializer_class tells the ViewSet how to convert model instances
    # into JSON data for the API.
    serializer_class = BookSerializer
