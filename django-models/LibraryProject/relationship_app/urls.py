from . import views
from django.urls import path, include
from django.views.generic.detail import DetailView
from .views import book_list
from .views import list_books

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]