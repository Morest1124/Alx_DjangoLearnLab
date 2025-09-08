from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Library



# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title
    
    
    
class Library(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='library')
    
    def __str__(self):
        return self.name
    
    
class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="Librarian")
    
    def __str__(self):
        return self.name
    
    
# Define the user roles as choices
ROLES_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

class UserProfile(models.Model):
    """
    Extends the Django User model to include a role for role-based access control.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES_CHOICES, default='Member')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a UserProfile automatically when a new User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to save the UserProfile when the User is saved.
    """
    instance.userprofile.save()