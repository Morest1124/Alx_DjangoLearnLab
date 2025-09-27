from rest_framework import generics
from .Serializer import BookSerializer
from .models import Book, Author

# --- Book CRUD Views ---

class BookListCreate(generics.ListCreateAPIView):
    """Handles GET (list) and POST (create)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET (detail), PUT/PATCH (update), and DELETE (destroy)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer