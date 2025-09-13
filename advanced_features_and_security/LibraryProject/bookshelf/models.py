from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib import admin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="customuser",
    )

    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=2022)

class CustomPermission(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='custom_permissions')

    can_add_books = models.BooleanField(default=False)  
    can_delete_books = models.BooleanField(default=False)
    can_view_books = models.BooleanField(default=False)
    can_edit_books = models.BooleanField(default=False)

    can_create = models.BooleanField(default=False)

    can_delete_users = models.BooleanField(default=False)
    can_view_users = models.BooleanField(default=False)
    can_edit_users = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Custom Permission"
        verbose_name_plural = "Custom Permissions"  

    def __str__(self):

        return "Custom Permissions"


admin.site.register(CustomUser)
admin.site.register(Book)
admin.site.register(CustomPermission)