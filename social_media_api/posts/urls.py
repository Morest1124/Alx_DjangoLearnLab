# posts/urls.py

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path, include

# 1. Standard Router for Posts
router = DefaultRouter()
router.register(r'posts', PostViewSet)



urlpatterns = [
    #post routes: /posts/, /posts/{id}/, /posts/{id}/comments/    
    path('', include(router.urls)), 
    
    # Comment routes: /comments/, /comments/{id}/
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
]