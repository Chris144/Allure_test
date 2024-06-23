import unittest

from Projekt.locators.locators import SortLocators
from Projekt.pages.home_page import HomePage
from Projekt.pages.sort_page import SortPage
from Projekt.tests.test_base import BaseTest


class SortingTest(BaseTest,unittest.TestCase):
    """
        Test checking sorting by:
            - popularity
            - newness
            - average rating
    """
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.sort_page = SortPage(self.driver)

    def test_checking_sorting_by_popularity(self):
        """
        TC 001: Test checking sorting by popularity:
        """
        self.home_page.choose_menu()
        self.sort_page.click_on_sorting_list()
        self.sort_page.select_sorting_by_popularity()
        # Checking expected effects using assertions
        sort_popularity = self.driver.find_element(*SortLocators.OPTION_POPULARITY)
        self.assertEqual("Sort by popularity", sort_popularity.text)
        print(sort_popularity.text)
        self.home_page.screenshot()

    def test_checking_sorting_by_newness(self):
        """
        TC 002: Test checking sorting by newness:
        """
        self.home_page.choose_menu()
        self.sort_page.click_on_sorting_list()
        self.sort_page.select_sorting_by_newness()
        # Checking expected effects using assertions
        sort_newness = self.driver.find_element(*SortLocators.OPTION_NEWNESS)
        self.assertEqual("Sort by newness", sort_newness.text)
        print(sort_newness.text)
        self.home_page.screenshot()

    def test_checking_sorting_by_average(self):
        """
        TC 003: Test checking sorting by average:
        """
        self.home_page.choose_menu()
        self.sort_page.click_on_sorting_list()
        self.sort_page.select_sorting_by_average()
        # Checking expected effects using assertions
        sort_average = self.driver.find_element(*SortLocators.OPTION_AVERAGE)
        self.assertEqual("Sort by average rating", sort_average.text)
        print(sort_average.text)
        self.home_page.screenshot()

    def tearDown(self):
        BaseTest.tearDown(self)
