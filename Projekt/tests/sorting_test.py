import unittest

import allure

from Projekt.locators.locators import SortLocators
from Projekt.pages.home_page import HomePage
from Projekt.pages.sort_page import SortPage
from Projekt.tests.test_base import BaseTest


class SortingTest(BaseTest, unittest.TestCase):
    """
        Test checking sorting by:
            - popularity
            - newness
            - average rating
    """

    def setUp(self):
        super().setUp()
        with allure.step('Initialize page'):
            self.home_page = HomePage(self.driver)
        with allure.step('Initialize add to cart page'):
            self.sort_page = SortPage(self.driver)
        with allure.step('Initialize add to attach screenshot'):
            self.base_test = BaseTest

    @allure.story('Sorting product')
    @allure.severity(allure.severity_level.NORMAL)
    def test_checking_sorting_by_popularity(self):
        """
        TC 001: Test checking sorting by popularity:
        """
        with allure.step('Choose menu'):
            self.home_page.choose_menu()
            self.base_test.attach_screenshot(self, name='Choose menu')
        with allure.step('Click on sorting list'):
            self.sort_page.click_on_sorting_list()
            self.base_test.attach_screenshot(self, name='Click on sorting list')
        with allure.step('Select_sorting_by_popularity'):
            self.sort_page.select_sorting_by_popularity()
            self.base_test.attach_screenshot(self,name='Select_sorting_by_popularity')
        # Checking expected effects using assertions
        with allure.step('Verify sorting option'):
            sort_popularity = self.driver.find_element(*SortLocators.OPTION_POPULARITY)
            self.assertEqual("Sort by popularity1", sort_popularity.text)
            print(sort_popularity.text)
            self.base_test.attach_screenshot(self, name='Verify sorting option')
        with allure.step('Screenshot_select_sorting_by_popularity'):
            self.base_test.attach_screenshot(self, name='Screenshot_select_sorting_by_popularity')
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
