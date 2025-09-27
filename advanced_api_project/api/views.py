from .Serializer import BookSerializer
from .models import Book, Author
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# --- Book CRUD Views ---

class BookListCreate(generics.ListCreateAPIView):
    """Handles GET (list) and POST (create)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name'] 


    # Allows GET requests for anyone, but requires authentication for POST.
    permission_classes = [IsAuthenticatedOrReadOnly] 

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET (detail), PUT/PATCH (update), and DELETE (destroy)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

    # Allows GET requests for anyone, but requires authentication for PUT, PATCH, and DELETE.
    permission_classes = [IsAuthenticatedOrReadOnly]