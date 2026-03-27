from django import forms
from .models import Book, UserProfile

class BookForm(forms.ModelForm):
    """
    Form for creating and updating Book instances.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']