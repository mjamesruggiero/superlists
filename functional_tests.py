from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Alice has heard about a cool new online todo app.
        She goes to check out its homepage"""
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mention todos
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a todo item straight away

        # She types in "Buy peacock feathers" into a text box

        # When she hits enter, the page updates

        # There is still a text box inviting her to enter another item
        # She enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Alice wonders whether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her.
        # There is some explanatory text to that effect.

        # She visits that URL, her list is still there

        # satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
