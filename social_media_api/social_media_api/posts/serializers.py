

from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    # Read-only field to display the commenter's username
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'post'] # Post and author set by the view

class PostSerializer(serializers.ModelSerializer):
    # Read-only field to display the author's username
    author_username = serializers.CharField(source='author.username', read_only=True)
    
    # Nested field to display comments
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at', 'comments_count']
        read_only_fields = ['author'] 

    def get_comments_count(self, obj):
        return obj.comments.count()