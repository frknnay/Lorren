import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from books.models import Book
from authors.models import Author

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def create_a_book_with_author(self):
        author = Author.objects.create(name='J.R.R. Tolkien')
        book = Book.objects.create(
                    title='Silmarillion', author=author, year=1977
                )
        return book

    def create_author(self, name):
        author = Author.objects.create(name=name)
        return author

    def create_book(self, title, author, year):
        book = Book.objects.create(title=title, author=author, year=year)
        return book
