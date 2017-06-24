from django.test import TestCase
from books.models import Book
from authors.models import Author

class HomePageTest(TestCase):

    def test_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'books/home.html')

    def test_books_are_listed_on_home_page(self):
        author = Author.objects.create(name='J.R.R. Tolkien')
        Book.objects.create(title='The Hobbit', author=author, year=1937)
        response = self.client.get('/')
        self.assertContains(response, 'The Hobbit')

class BookDetailPageTest(TestCase):

    def test_renders_detail_page_template(self):
        author = Author.objects.create(name='J.R.R. Tolkien')
        book = Book.objects.create(title='Hobbit', author=author, year=1937)
        response = self.client.get(f'/books/show/{book.id}/')
        self.assertTemplateUsed(response, 'books/book_detail.html')
