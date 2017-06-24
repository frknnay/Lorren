from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_get_details_of_a_book(self):
        ## We create a random book to be able to test some of our functionalities
        book = self.create_a_book_with_author()

        # Kvothe hears about a web-app called Lorren.
        # He goes to check out it's homepage.
        self.browser.get(self.live_server_url)

        # He notices that the page title mention Lorren app.
        self.assertIn('Lorren', self.browser.title)

        # Then he sees that there is a list of some books and he clicks on the
        # name of first book.
        self.wait_for(
            lambda: self.browser.find_element_by_link_text(book.title).click()
        )

        # He also notices that he redirected to a page with the details of book
        # And he sees that the name of the book is written in page title
        self.wait_for(
            lambda: self.assertIn(book.title, self.browser.title)
        )
        # He also can see the name of the writer of the book in that page
        self.wait_for(
            lambda: self.assertIn(book.author.name, self.browser.find_element_by_tag_name('body').text)
        )
