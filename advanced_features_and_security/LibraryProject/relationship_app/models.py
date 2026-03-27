from django.db import models
from django.conf import settings
from django.contrib import admin

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    

# Book Model: Represents a book in the library
class Book(models.Model):
    title = models.CharField(max_length=30)
    # Establishes a many-to-one relationship with the Author model.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField(null=True, blank=True)
    
    class Meta:
        permissions = (
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        )
        # Defines custom permissions for the Book model.        
    
    def __str__(self):
        return self.title
    
    
   # Library Model: Represents a library that contains multiple books. 
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES_CHOICES, default='Member')

    def __str__(self):
        return self.user.username

# These functions are signal receivers. They listen for the 'post_save' event from the User model.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a UserProfile automatically when a new User is created.
    """
    if created:
        # When a new User instance is created, this automatically creates a corresponding UserProfile.
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to save the UserProfile when the User is saved.
    """
    # When the User instance is saved, this ensures its associated UserProfile is also saved.
    instance.userprofile.save()