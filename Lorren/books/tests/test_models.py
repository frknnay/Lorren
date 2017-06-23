from django.test import TestCase
from books.models import Book
from authors.models import Author

class BookModelTest(TestCase):

    def test_book_is_related_to_author(self):
        author = Author.objects.create(name='Ursula Poznanski')
        book = Book(title='Erebos',author=author,year=2010)
        book.save()
        self.assertIn(book, author.item_set.all())
