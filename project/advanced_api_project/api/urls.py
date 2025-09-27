from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy

urlpatterns = [
    # Endpoint: /books/
    # Maps to the BookListCreate view.
    path('books/', BookListCreate.as_view(), name='book-list-create'),

    # Endpoint: /books/<int:pk>/.
    # Maps to the BookRetrieveUpdateDestroy view.
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-detail-update-destroy'),
]