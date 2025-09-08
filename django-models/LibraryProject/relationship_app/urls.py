from . import views
from django.urls import path, include
from django.views.generic.detail import DetailView
from .views import book_list
from .views import list_books
from django.contrib.auth import views as auth_views


urlpatterns = [
    # In urls.py
    
    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    path('register/', views.register, name='register'),    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
     # URLs for the role-based dashboards
    path('admin/', views.admin_view, name='admin_dashboard'),    

    path('librarian/', views.librarian_view, name='librarian_dashboard'),    
    path('member/', views.member_view, name='member_dashboard'),
    
    
    # URLs for the Book CRUD operations
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),

]