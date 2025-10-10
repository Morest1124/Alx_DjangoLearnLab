
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

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
            serializer.save(author=self.request.user, post=post)
        else:
            
            serializer.save(author=self.request.user)