from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class AuthorTest(FunctionalTest):

    def test_can_add_new_author(self):
        # Kvothe want's to add new authors to lorren app.
        # So he goes to author creation link.
        self.browser.get(self.live_server_url + '/authors/new')

        # He notices that there is a inputbox that he can enter a name for
        # the new author that he wants to add then he enters "Alber Camus"
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Albert Camus')
        inputbox.send_keys(Keys.ENTER)

        # Then he goes to authors page to see if his new author added to the system
        response = self.browser.get(self.live_server_url + '/authors/')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Albert Camus', page_text)
