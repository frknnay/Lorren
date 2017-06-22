from django.test import LiveServerTestCase

from selenium import webdriver


class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_new_visitor(self):
        # Kvothe heards about a web-app called Lorren.
        # He goes to check out it's homepage.
        self.browser.get(self.live_server_url)

        # He notices that the page title and header mention Lorren app.
        self.assertIn('Lorren', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Lorren', header_text)
