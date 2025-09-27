from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.Model(max_length =100)
    publication_year = models.IntegerField(blank=False)
    #one-to-many realationship
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    class Meta:
        model = models