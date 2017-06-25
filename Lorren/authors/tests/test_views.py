from django.test import TestCase
from books.models import Book
from authors.models import Author

class AuthorDetailViewTest(TestCase):

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

class AddNewAuthorViewTest(TestCase):

    def test_uses_add_author_template(self):
        response = self.client.get('/authors/new')
        self.assertTemplateUsed(response, 'authors/add_author.html')

    def test_can_add_new_author(self):
        self.client.post(
            '/authors/new',
            data={'name': 'Albert Camus'}
        )
        self.assertEqual('Albert Camus', Author.objects.first().name)

class EditAuthorViewTest(TestCase):

    def test_uses_edit_author_template(self):
        author = Author.objects.create(name='Albert Camus')
        response = self.client.get(f'/authors/show/{author.id}/edit')
        self.assertTemplateUsed(response, 'authors/edit_author.html')

    def test_edit_page_has_details_of_author(self):
        author = Author.objects.create(name='Albert Camus')
        response = self.client.get(f'/authors/show/{author.id}/edit')
        self.assertContains(response, author.name)

    def test_edit_page_can_edit_details_of_author(self):
        author = Author.objects.create(name='Albert')
        self.client.post(
            f'/authors/show/{author.id}/edit',
            data={'name': 'Albert Camus'}
        )
        author = Author.objects.get(id=author.id)
        self.assertEqual(author.name, 'Albert Camus')

class DeleteAuthorViewTest(TestCase):

    def test_deletes_existing_author(self):
        author = Author.objects.create(name="Albert Camus")
        self.client.get(f'/authors/show/{author.id}/delete')
        self.assertNotIn(author, Author.objects.all())
