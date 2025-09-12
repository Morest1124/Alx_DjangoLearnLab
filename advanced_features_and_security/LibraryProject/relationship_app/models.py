from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES_CHOICES, default='Member')

    def __str__(self):
        return self.user.username

# These functions are signal receivers. They listen for the 'post_save' event from the User model.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a UserProfile automatically when a new User is created.
    """
    if created:
        # When a new User instance is created, this automatically creates a corresponding UserProfile.
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to save the UserProfile when the User is saved.
    """
    # When the User instance is saved, this ensures its associated UserProfile is also saved.
    instance.userprofile.save()


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email' # Use email as the unique identifier for authentication
    REQUIRED_FIELDS = []    # No additional fields are required for user creation
    
    # The __str__ method is commented out, but if uncommented, it would return the user's email.
    # def __str__(self):
    #     return self.email
    

    class CustomUserManager(BaseUserManager):

        # Custom user creation method
        def customeUser(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError('The Email field must be set')
            email = self.normalize_email(email) # Normalize the email address for consistency
            user = self.model(email=email, **extra_fields) # Create a new user instance
            user.set_password(password) # Set the user's password
            user.save(using=self._db) # Save the user to the database

            # Return the created user

            return user

        # Custom superuser creation method
        def create_superuser(self, email, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_active', True)
            extra_fields.setdefault('is_admin', True)
            # Ensure that the superuser has staff and superuser permissions

            if extra_fields.get('is_staff') is not True:
                raise ValueError('Superuser must have is_staff=True.')
            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must have is_superuser=True.')

            # Create and return the superuser using the custom user creation method
            return self.customeUser(email, password, **extra_fields)


    objects = CustomUserManager() # Assign the custom manager to the objects attribute

    def __str__(self):
        return self.email

    class ModelAdmin(admin.ModelAdmin):
        list_display = ('email', 'is_staff', 'is_superuser', 'is_active', 'is_admin')
        search_fields = ('email',)
        list_filter = ('is_staff', 'is_superuser', 'is_active')
        ordering = ('email',)
        filter_horizontal = ()
        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'fields': ('date_of_birth', 'profile_picture')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )     add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'date_of_birth', 'profile_picture', 'password1', 'password2'),
            }),
        )
        
