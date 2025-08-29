
    book_to_delete = Book.object(id=Book.id)
    print(f"You are about to delete: {book_to_delete}")
    You are about to delete 1984
    
    book_to_delete.delete()
    (1, {'library.Book': 1})
    
    try:
        book_to_delete = Book.object(id=Book.id)
    except Book.DoesNotExsist:
        print("Book successfully deleted!")
    Book successfully deleted!