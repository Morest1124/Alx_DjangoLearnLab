from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    boi = models.CharField(blank= True)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='Following')
    
    def __str__(self):
        return self.username