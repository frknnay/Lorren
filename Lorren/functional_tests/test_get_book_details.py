from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_get_details_of_a_book(self):
        # Kvothe heards about a web-app called Lorren.
        # He goes to check out it's homepage.
        self.browser.get(self.live_server_url)

        # He notices that the page title and header mention Lorren app.
        self.assertIn('Lorren', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Lorren', header_text)

        # Then he sees that there is a list of some books and he clicks on the
        # name of first book.
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Silmarillion').click()
        )

        # He notices that he directed to a page with the details of book
        self.assertIn('Silmarillion', self.browser.title)

        self.fail('finish the test')
