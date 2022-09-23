import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        # download chrome driver and place it into your path https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/
        # in mac make chromedriver runnable by setting perm: xattr -d com.apple.quarantine path/chromedriver
        # install geckodriver: brew install geckodriver
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.implicitly_wait(3)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        # user has heard about a cool new online to-do app, she goes to checkout its homepage
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')

        # she types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # there is still a text box inviting her to add another item. she
        # enters "Use peaco0ck feathers to make a fly"

        # the page updates again, and now shows both items on her list

        # she wonders whether the site will remember her list. then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect

        # she visists that url - here to-do list is still there

        # statisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
