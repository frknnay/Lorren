from django.test import TestCase
from django.core.exceptions import ValidationError

from books.models import Book
from authors.models import Author

class AuthorModelTest(TestCase):

    def test_cannot_save_empty_author(self):
        author = Author()
        with self.assertRaises(ValidationError):
            author.save()
            author.full_clean()
