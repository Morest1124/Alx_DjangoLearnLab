from django.contrib import admin
from .models import models

# Register your models here.

@admin.register(models)
class modelsAdmin(admin.ModelAdmin):
    Book = ('title', 'author', 'publication_year')

    
    
    
