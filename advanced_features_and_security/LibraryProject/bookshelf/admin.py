from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.

@admin.register(Book)
class modelsAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_of_birth', 'is_staff')
    search_fields = ('email', 'date_of_birth')

admin.site.register(CustomUser, CustomUserAdmin)