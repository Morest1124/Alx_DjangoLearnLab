from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=200, required=False, help_text='Enter tags separated by commas')
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tags'].initial = ', '.join([tag.name for tag in self.instance.tags.all()])
    
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            # Handle tags
            tags_text = self.cleaned_data.get('tags', '')
            if tags_text:
                tag_names = [name.strip() for name in tags_text.split(',') if name.strip()]
                post.tags.clear()
                for tag_name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)
            else:
                post.tags.clear()
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
