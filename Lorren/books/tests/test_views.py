from django.test import TestCase


class HomePageTest(TestCase):

    def test_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'books/home.html')
