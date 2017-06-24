from django.test import TestCase
from django.core.exceptions import ValidationError

from books.models import Book
from authors.models import Author

class BookModelTest(TestCase):

    def test_book_is_related_to_author(self):
        author = Author.objects.create(name='Ursula Poznanski')
        book = Book(title='Erebos',author=author,year=2010)
        book.save()
        self.assertIn(book, author.book_set.all())

    def test_cannot_save_empty_book(self):
        book = Book()
        with self.assertRaises(ValidationError):
            book.full_clean()

    def test_cannot_save_book_without_author(self):
        book = Book(title="Test book", year=2000)
        with self.assertRaises(ValidationError):
            book.full_clean()
