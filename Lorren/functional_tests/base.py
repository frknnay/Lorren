import time
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from books.models import Book

MAX_WAIT = 10

class FunctionalTest(LiveServerTestCase):

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

    def create_a_book(self):
        book = Book.objects.create(
                    title="Silmarillion", author='J.R.R Tolkien', year=1885
                )
        return book
