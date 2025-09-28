from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# A ListView for retrieving all books.
class BookListView(generics.ListAPIView):
    """
    API endpoint that allows listing all books with filtering, searching, and ordering capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Set up filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Fields available for filtering
    # Example: /api/books/?publication_year=2023
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Fields available for searching
    # Example: /api/books/?search=Django
    search_fields = ['title', 'author__name']
    
    # Fields available for ordering
    # Example: /api/books/?ordering=publication_year or /api/books/?ordering=-publication_year
    ordering_fields = ['title', 'publication_year']

# A DetailView for retrieving a single book by ID.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# A CreateView for adding a new book.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# An UpdateView for modifying an existing book.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# A DeleteView for removing a book.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
