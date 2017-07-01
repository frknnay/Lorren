from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


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

    def test_can_edit_existing_author(self):
        # Kvothe want's to add another author to system
        self.browser.get(self.live_server_url + '/authors/new')

        # He types 'George Orwel'
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('George Orwel')
        inputbox.send_keys(Keys.ENTER)

        # Then he realises that he mistyped the name. Knowing that he want's to
        # edit the name of the author
        self.browser.get(self.live_server_url + '/authors/show/2/edit')
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('l')
        inputbox.send_keys(Keys.ENTER)

        # He sees that the old name changed to new one
        self.browser.get(self.live_server_url + '/authors/show/2/')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('George Orwell', page_text)

class BookTest(FunctionalTest):

    def test_can_add_new_book(self):
        ## To add a book, we first need to add an Author.
        author = self.create_author(name='Patrick Rothfuss')

        # Kvothe wants to add new book so that he goes to new_book page
        self.browser.get(self.live_server_url + '/books/new')

        # He sees that there are two inputboxes for title and year for the new
        # book that he wants to add. And there is also a drop down list to
        # select an author for the book. Then he starts to type...

        inputbox_title = self.browser.find_element_by_id('id_title')
        inputbox_title.send_keys('The Wise Man\'s Fear')

        drop_down_list = Select(self.browser.find_element_by_id('id_author'))
        drop_down_list.select_by_visible_text('Patrick Rothfuss')

        inputbox_year = self.browser.find_element_by_id('id_year')
        inputbox_year.send_keys('2011')
        inputbox_year.send_keys(Keys.ENTER)

        # Then he goes to home page to see if his new book added to the system
        response = self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('The Wise Man\'s Fear', page_text)

        self.fail('finish test!')
