from rest_framework import serializers
from .models import Book
from .models import Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = '_all_'
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = 'name'
    

    
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value