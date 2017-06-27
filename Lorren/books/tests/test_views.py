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

class EditBookViewTest(TestCase):

    def test_uses_edit_book_template(self):
        author = Author.objects.create(name='Stefan Zweig')
        book = Book.objects.create(title='Chess', author=author, year=1941)
        response = self.client.get(f'/books/show/{book.id}/edit')
        self.assertTemplateUsed(response, 'books/edit_book.html')

    def test_edit_page_has_details_of_book(self):
        author = Author.objects.create(name='Stefan Zweig')
        book = Book.objects.create(title='Chess', author=author, year=1941)
        response = self.client.get(f'/books/show/{book.id}/edit')
        self.assertContains(response, book.title)

    def test_edit_page_can_edit_details_of_book(self):
        author = Author.objects.create(name='Stefan Zweig')
        book = Book.objects.create(title='Chess', author=author, year=1941)
        self.client.post(
            f'/books/show/{book.id}/edit',
            data={'title': 'The world of yesterday', 'year': 1942}
        )
        book = Book.objects.get(id=book.id)
        self.assertEqual(book.title, 'The world of yesterday')

    def test_deletes_existing_book(self):
        author = Author.objects.create(name='Stefan Zweig')
        book = Book.objects.create(title='Chess', author=author, year=1941)
        self.client.get(f'/books/show/{book.id}/delete')
        self.assertNotIn(book, Book.objects.all())
