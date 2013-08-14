#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
from superlists import settings
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Alex open the homepage
        self.browser.get('http://localhost:8000')
        # Alex looks for expected title
        self.assertIn(
            settings.SITE_NAME, self.browser.title,
            'Browser title was %s' % self.browser.title)

        self.fail('TODO: Finish the test!')

if __name__ == '__main__':
    unittest.main()
