import unittest

import allure
from selenium import webdriver
from Projekt.pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        self.driver.implicitly_wait(5)
        self.home_page = HomePage(self.driver)

    def test_checking_hoover_on_account(self):
        self.home_page = HomePage(self.driver)
        self.home_page.hoover_on_account()
        self.home_page.screenshot()

    def attach_screenshot(self,name):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

    def tearDown(self):
        self.driver.quit()



