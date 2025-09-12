from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib import admin

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=2022)
    
    
 
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email' # Use email as the unique identifier for authentication
    REQUIRED_FIELDS = []    # No additional fields are required for user creation
    
    # The __str__ method is commented out, but if uncommented, it would return the user's email.
    # def __str__(self):
    #     return self.email
    

    class CustomUserManager(BaseUserManager):

        # Custom user creation method
        def create_user(self, email, password=None, **extra_fields):
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
            return self.create_user(email, password, **extra_fields)


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
        
    class CustomPermission(models.Model):

        can_add_books = models.BooleanField(default=False)  
        can_delete_books = models.BooleanField(default=False)
        can_view_books = models.BooleanField(default=False)
        can_edit_books = models.BooleanField(default=False)

        can_create_users = models.BooleanField(default=False)

        can_delete_users = models.BooleanField(default=False)
        can_view_users = models.BooleanField(default=False)

        can_edit_users = models.BooleanField(default=False)

        class Meta:
            verbose_name = "Custom Permission"

            verbose_name_plural = "Custom Permissions"  

    def __str__(self):
        return "Custom Permissions"