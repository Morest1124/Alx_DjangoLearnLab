from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book, Author, Library
# Create your views here.

# Function-based view
def book_list(request):
    """Get all books and authors."""
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {'books': books, 'authors': authors}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view
class BookDetailView(DetailView):
    """Get a single book and display its details."""
    model = Book
    template_name = 'relationship_app/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        """Inject additional context, like the average rating, into the template."""
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        # Ensure the `get_average_rating` method exists on the Book model
        # or implement it here if it's not a model method.
        # context['average_rating'] = book.get_average_rating()
        return context

# A potential Class-based Library DetailView based on the prompt's instructions
class LibraryDetailView(DetailView):
    """Display details for a specific library, including its books."""
    model = Library
    template_name = 'libraries/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add all books related to this library to the context."""
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_in_library'] = library.books.all() # Assuming a reverse relationship from Library to Book
        return context