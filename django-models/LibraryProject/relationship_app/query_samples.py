# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """
    Queries all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        author = Author.objects.filter(author=author)
        books = author.book_set.all()  # Use the default related_name or the one you defined
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

def get_books_in_library(library_name):
    """
    Lists all books in a library.
    """
    try:
        library = Library.objects.filter(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library.name} Library:")
        for book in books:
            print(f"- {book.title} (by {book.author.name})")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def get_librarian_for_library(library_name):
    """
    Retrieves the librarian for a library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian.all()
        print(f"\nLibrarian for {library.name} Library:")
        print(f"- {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}'.")

if __name__ == '__main__':
    # --- Example Usage ---

    # Make sure you have some data in your database.
    # For example, you can use the Django shell to create these objects:
    # >>> from relationship_app.models import Author, Book, Library, Librarian
    # >>> author1 = Author.objects.create(name='J.K. Rowling')
    # >>> book1 = Book.objects.create(title='Harry Potter and the Sorcerer\'s Stone', author=author1)
    # >>> book2 = Book.objects.create(title='Harry Potter and the Chamber of Secrets', author=author1)
    # >>> library1 = Library.objects.create(name='Central Library')
    # >>> library1.books.add(book1, book2)
    # >>> librarian1 = Librarian.objects.create(name='Ms. Eleanor Vance', library=library1)
    
    get_books_by_author('J.K. Rowling')
    get_books_in_library('Central Library')
    get_librarian_for_library('Central Library')