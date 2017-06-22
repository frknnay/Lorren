from django.test import TestCase
from books.models import Book

class HomePageTest(TestCase):

    def test_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'books/home.html')

    def test_books_are_listed_on_home_page(self):
        Book.objects.create(title='Hobbit', author='Tolkien', year=1991)
        response = self.client.get('/')
        self.assertContains(response, 'Hobbit')

class BookDetailPageTest(TestCase):

    def test_renders_detail_page_template(self):
        book = Book.objects.create(title='Hobbit', author='Tolkien', year=1991)
        response = self.client.get(f'/books/{book.id}/')
        self.assertTemplateUsed(response, 'books/book_detail.html')
