import time
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from books.models import Book

MAX_WAIT = 10

class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        ## We create a random book to be able to test some of our functionalities
        Book.objects.create(
            title="Silmarillion", writer='J.R.R Tolkien', year=1885
        )

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
