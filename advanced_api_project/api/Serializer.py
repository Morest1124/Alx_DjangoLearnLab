from rest_framework import serializers
from .models import Book, Author
from datetime import date # Changed from 'datetime' to 'date' for clarity and efficiency

# Purpose: Serializes the Author model data. 
# It is used for displaying Author lists or details, and for creating/updating Author records.
class AuthorSerializer(serializers.ModelSerializer):
    # The 'books' field will automatically be added if 'fields = "__all__"' is used, 
    # but we are focusing on 'name' as requested.
    class Meta:
        model = Author
        fields = ('id', 'name') # Changed 'field' to 'fields' and used a tuple

# Purpose: Serializes the Book model data. 
# It handles conversion between complex Book objects and simple Python datatypes (like JSON).
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__' # Corrected 'field' to 'fields'

    # Field-level validation for 'publication_year'. 
    # Purpose: Ensures the publication year is not set to a year in the future.
    def validate_publication_year(self, value):
        # Using date.today().year for the current year
        current_year = date.today().year 
        
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        return value