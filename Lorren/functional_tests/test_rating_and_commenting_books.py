from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class RateTest(FunctionalTest):

    def test_can_rate_book(self):
        self.create_a_book_with_author()

        # Kvothe wants to rate one of his favorite books. So he goes to it's page
        self.browser.get(self.live_server_url + '/books/show/1')

        # He wants to give book 9 points so he chooses 9 from selection box then
        # clicks rate button next to it.
        drop_down_list = Select(self.browser.find_element_by_id('id_rate_point'))
        drop_down_list.select_by_visible_text('9')

        self.browser.find_element_by_id('id_rate_btn').click()

        # Then he sees that the rating of the book has changed
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element_by_id('id_book_rate').text,
                '9.0')
        )
