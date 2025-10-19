from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import PostCreateView, PostUpdateView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('tag/<str:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]