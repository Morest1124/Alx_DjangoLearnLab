from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    
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
    