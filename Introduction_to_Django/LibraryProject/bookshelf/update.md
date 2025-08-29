book_to_update = Book.object.get(id=Book.id)
print(f"The current title: {bool_to_update.title}")
The current tite: 1946

book_to_update.book.title = "Nineteen Eighty-Four"
book_to_update.save()
print(f"(Updated book title: {book_to_update.title})")
Updated book title: "Nineteen Eighty-Four"

