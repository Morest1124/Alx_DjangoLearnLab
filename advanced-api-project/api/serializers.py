from rest_framework import serializers
from .models import Book, Author
from datetime import date 
# Purpose: Serializes the Author model data. 
class AuthorSerializer(serializers.ModelSerializer):
    
    # The 'books' field will automatically be added if 'fields = "__all__"' is used, 
    class Meta:
        model = Author
        fields = ('id', 'name') # Changed 'field' to 'fields' and used a tuple

# It handles conversion between complex Book objects and simple Python datatypes.
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__' # Corrected 'field' to 'fields'
        
    # Purpose: Ensures the publication year is not set to a year in the future.
    def validate_publication_year(self, value):
        # Using date.today().year for the current year
        current_year = date.today().year 
        
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        return value