from .Serializer import BookSerializer
from .models import Book, Author
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# --- Book CRUD Views ---
class BookListCreate(generics.ListCreateAPIView):
    """
    API endpoint that allows listing all books and creating a new book.

    Permissions:
        - Read-only access (GET): Allowed for unauthenticated users.
        - Write access (POST): Requires authenticated users (IsAuthenticatedOrReadOnly).

    Methods Handled:
        - GET /books/: Returns a list of all Book instances.
        - POST /books/: Creates a new Book instance.

    Customizations:
        - Utilizes SearchFilter and OrderingFilter for enhanced list retrieval.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name'] 


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows retrieving, updating, or deleting a single book.

    Permissions:
        - Read-only access (GET): Allowed for unauthenticated users.
        - Write access (PUT, PATCH, DELETE): Requires authenticated users (IsAuthenticatedOrReadOnly).

    Methods Handled:
        - GET /books/{pk}/: Retrieves the details of a single Book.
        - PUT /books/{pk}/: Fully updates the Book instance.
        - PATCH /books/{pk}/: Partially updates the Book instance.
        - DELETE /books/{pk}/: Deletes the Book instance.

    Lookup Field:
        - Uses the default primary key ('pk') for object lookup.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]