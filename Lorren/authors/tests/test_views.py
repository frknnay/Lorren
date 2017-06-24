from django.test import TestCase
from books.models import Book
from authors.models import Author

class AuthorDetailPage(TestCase):

    def test_uses_author_detail_template(self):
        author = Author.objects.create(name="Nazım Hikmet")
        response = self.client.get('/authors/show/{author.id}')
        self.assertTemplateUsed(response, 'authors/author_detail.html')
