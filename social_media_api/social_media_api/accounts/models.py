from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.CharField(blank= True)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='Following')
    followering = models.ManyToManyField('self', symmetrical=False, related_name='Follower')
    
    def __str__(self):
        return self.username