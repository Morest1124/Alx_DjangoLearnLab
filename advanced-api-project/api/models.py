# api/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)

    publication_year = models.IntegerField()

    # all their books are also deleted.
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name='books' # Allows Author objects to query their books
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
