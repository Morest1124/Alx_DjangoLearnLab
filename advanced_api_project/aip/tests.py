# from django.test import TestCase
# # from aip.Serializer import Serializers
# from aip.models import models, Book, 

# # Create your tests here.
# import datetime
# from unittest.mock import patch
# # ... import your Serializer/Class

# def test_future_year_validation_error(self):
#     # Mock the current date to be a specific date
#     with patch('datetime.date') as mock_date:
#         mock_date.today.return_value = datetime.date(2023, 1, 1) # Sets current year to 2023
#         mock_date.today.year = 2023 # Also set the year property for direct access

#         validator_instance = Book()
#         # Test a future year
#         with self.assertRaises(serializers.ValidationError):
#             validator_instance.validate_publication_year(2024)

#         # Test a valid year
#         result = validator_instance.validate_publication_year(2023)
#         self.assertEqual(result, 2023)