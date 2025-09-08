from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import Book, Author, Library, UserProfile
from .forms import BookForm

# Create your views here.

# Function-based view
def list_books(request):
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
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add all books related to this library to the context."""
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_in_library'] = library.books.all() # Assuming a reverse relationship from Library to Book
        return context
    
  
def register(request):
    # Check if the form has been submitted
    if request.method == 'POST':
        # Create a form instance from the submitted data
        form = UserCreationForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Save the new user to the database
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # Redirect to the login page
            return redirect('login')
    # If it's a GET request (or form is invalid)
    else:
        # Create an empty form instance
        form = UserCreationForm()
    
    # Render the registration page with the form
    return render(request, 'relationship_app/register.html', {'form': form})


# Test functions for user roles
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    """
    View for administrators. Accessible only to users with the 'Admin' role.
    """
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

@user_passes_test(is_librarian)
def librarian_view(request):
    """
    View for librarians. Accessible only to users with the 'Librarian' role.
    """
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

@user_passes_test(is_member)
def member_view(request):
    """
    View for members. Accessible only to users with the 'Member' role.
    """
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View for adding a new book. Only users with the 'can_add_book' permission can access.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('list_books') # Redirect to a book list page
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    """
    View for editing an existing book. Only users with the 'can_change_book' permission can access.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    """
    View for deleting a book. Only users with the 'can_delete_book' permission can access.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})
