from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permession to only allow authors of an object to edit or delete it.
    Read permissions are allowed to any user.
    """
    def has_object_permission(self, request, view, obj):
        # Read permessions are allowed to any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #Permissions are only allowed to the uthor of the post/comment.
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    """Provides CRUD operations for Posts, including listing comments."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    
    # Implement Pagination and Filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'content'] # Filtering by title or content
    
    def perform_create(self, serializer):
        # Automatecally set the author to the currently logged-in User
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def feed(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)

    # Custom action to list comments for a specific post
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    """Provides CRUD operations for Comments."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        #Filter comments to only show those for a specific post if the post_pk is provided
        if 'post_pk' in self.kwargs:
            return self.queryset.filter(post=self.kwargs['post_pk'])
        return self.queryset
    
    def perform_create(self, serializer):
        if 'post_pk' in self.kwargs:
            post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
            comment = serializer.save(author=self.request.user, post=post)
            
            # Create notification
            if post.author != self.request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=self.request.user,
                    verb='commented on',
                    target=comment
                )
        else:
            serializer.save(author=self.request.user)

class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)

class UnlikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)