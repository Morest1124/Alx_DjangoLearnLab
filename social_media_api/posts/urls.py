# posts/urls.py

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeView, UnlikeView
from django.urls import path, include

# Standard Router for Posts
router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("feed/", PostViewSet.as_view({'get': 'feed'}), name='post-feed'),
    path('posts/<int:pk>/like/', LikeView.as_view(), name='like'),
    path('posts/<int:pk>/unlike/', UnlikeView.as_view(), name='unlike'),
    #post routes: /posts/, /posts/{id}/, /posts/{id}/comments/    
    path('', include(router.urls)), 
    
    # Comment routes: /comments/, /comments/{id}/
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
]
