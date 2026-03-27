from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITests(APITestCase):
    def setUp(self):
        # Create an author and a book for testing
        self.author = Author.objects.create(name="Morest Burawa")
        self.book = Book.objects.create(
            title="Test Book", author=self.author, publication_year=2023
        )
        # Create a user for authentication tests
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_book_list_view(self):
        """
        Ensure we can retrieve the list of books.
        """
        url = reverse("book-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_book_detail_view(self):
        """
        Ensure we can retrieve a single book.
        """
        url = reverse("book-detail", kwargs={"pk": self.book.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book(self):
        """
        Ensure we can create a new book.
        """
        self.client.login(username="testuser", password="testpassword")
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "author": self.author.pk,
            "publication_year": 2024,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """
        Ensure we can update an existing book.
        """
        self.client.login(username="testuser", password="testpassword")
        url = reverse("book-update", kwargs={"pk": self.book.pk})
        data = {
            "title": "Updated Book",
            "author": self.author.pk,
            "publication_year": 2023,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        self.client.login(username="testuser", password="testpassword")
        url = reverse("book-delete", kwargs={"pk": self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_unauthenticated_user_cannot_create_book(self):
        """
        Ensure unauthenticated users cannot create a book.
        """
        url = reverse("book-create")
        data = {
            "title": "New Book by Unauthenticated User",
            "author": self.author.pk,
            "publication_year": 2024,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filtering_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        Book.objects.create(
            title="Another Book", author=self.author, publication_year=2024
        )
        url = reverse("book-list")
        response = self.client.get(url, {"publication_year": 2023}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_searching_by_title(self):
        """
        Test searching books by title.
        """
        Book.objects.create(
            title="Another Book", author=self.author, publication_year=2024
        )
        url = reverse("book-list")
        response = self.client.get(url, {"search": "Test Book"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_ordering_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        Book.objects.create(
            title="Older Book", author=self.author, publication_year=2022
        )
        url = reverse("book-list")
        response = self.client.get(url, {"ordering": "publication_year"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Older Book")
        self.assertEqual(response.data[1]["title"], "Test Book")
