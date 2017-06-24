from django.test import TestCase
from books.models import Book
from authors.models import Author

class AuthorDetailPage(TestCase):

    def test_uses_author_detail_template(self):
        author = Author.objects.create(name='Nazım Hikmet')
        response = self.client.get(f'/authors/show/{author.id}/')
        self.assertTemplateUsed(response, 'authors/author_detail.html')

    def test_display_author_details_on_detail_page(self):
        author = Author.objects.create(name='Nazım Hikmet')
        book = Book.objects.create(
            title='Henüz Vakit Varken Gülüm', author=author, year=1967
        )
        response = self.client.get(f'/authors/show/{author.id}/')

        self.assertContains(response, author.name)
        self.assertContains(response, author.book_set.all()[0])
