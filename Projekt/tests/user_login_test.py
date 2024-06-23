
import unittest
from Projekt.locators.locators import AccountLocators
from Projekt.pages.home_page import HomePage

from Projekt.pages.login_page import LoginPage
from Projekt.tests.test_base import BaseTest
from Projekt.test_data.data_faker_for_tests import AccountData
from ddt import ddt, data, unpack
from Projekt.test_data.read_Data_from_excel import ReadFile


@ddt
class TestLogin(BaseTest, unittest.TestCase):
    """
        Test checking user logging in various ways
    """

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.faker_data = AccountData()

    @data(ReadFile.get_test_data(0))
    @unpack
    def test_login_positive_enter_email(self, username_email, password):
        """
        TC 001: Test checking user login enter email - positive
        """
        self.home_page.click_account()
        self.login_page.enter_email(username_email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        self.home_page.screenshot()
        positive_login = self.driver.find_element(*AccountLocators.LOGIN_POSITIVE_USERNAME)
        self.assertEqual("Hello jaimechapman (not jaimechapman? Log out)", positive_login.text)
        print(positive_login.text)

    @data(ReadFile.get_test_data(1))
    @unpack
    def test_login_positive_enter_username(self, username_email, password):
        """
        TC 002: Test checking user login enter username - positive
        """
        self.home_page.click_account()
        self.login_page.enter_email(username_email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        self.home_page.screenshot()
        positive_login = self.driver.find_element(*AccountLocators.LOGIN_POSITIVE_USERNAME)
        self.assertEqual("Hello jaimechapman (not jaimechapman? Log out)", positive_login.text)
        print(positive_login.text)

    @data(ReadFile.get_test_data(2))
    @unpack
    def test_login_no_email(self, username_email, password):
        """
        TC 003: Test checking user login - empty field email
        """
        self.home_page.click_account()
        self.login_page.enter_email(username_email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        self.home_page.screenshot()
        # Checking the expected effect using assert
        error_mail = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
        self.assertEqual("Error: Username is required.", error_mail.text)
        print(error_mail.text)

    @data(ReadFile.get_test_data(3))
    @unpack
    def test_login_no_password(self, username_email, password):
        """
        TC 004: Test checking user login - empty field password
        """
        self.home_page.click_account()

        self.login_page.enter_email(username_email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        self.home_page.screenshot()
        # Checking the expected effect using assert
        error_password = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
        self.assertEqual("Error: The password field is empty.", error_password.text)
        print(error_password.text)

    @data(ReadFile.get_test_data(4))
    @unpack
    def test_login_user_not_registered_enter_username(self, username_email, password):
        """
        TC 005: Test checking user is not registered
        """
        self.home_page.click_account()
        self.login_page.enter_email(username_email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        self.home_page.screenshot()
        # Checking the expected effect using assert
        error_no_registered = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
        error_no_registered_username = (self.driver.find_element
                                        (*AccountLocators.ASSERT_REGISTRATION_NO_REGISTERED_USERNAME))
        self.assertEqual(
            f"Error: The username {error_no_registered_username.text} is not registered on this site."
            f" If you are unsure of your username, try your email address instead.",
            error_no_registered.text)
        print(error_no_registered.text)

    @data(ReadFile.get_test_data(5))
    @unpack
    def test_login_user_not_registered_enter_email(self, username_email, password):
        """
        TC 006: Test checking user is not registered
        """
        self.home_page.click_account()
        self.login_page.enter_email(username_email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        self.home_page.screenshot()
        # Checking the expected effect using assert
        error_no_registered = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
        self.assertEqual("Error: A user could not be found with this email address.", error_no_registered.text)
        print(error_no_registered.text)

    @data(ReadFile.get_test_data(6))
    @unpack
    def test_login_incorrect_password(self, username_email, password):
        """
        TC007: Test checking user login - incorrect password
        """
        self.home_page.click_account()
        self.login_page.enter_email(username_email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        self.home_page.screenshot()
        # Checking the expected effect using assert
        error_wrong_password = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
        error_wrong_password_username = self.driver.find_element(*AccountLocators.LOGIN_ERROR_USERNAME)
        self.assertEqual(
            f"Error: The password you entered for the username {error_wrong_password_username.text} is incorrect."
            f" Lost your password?", error_wrong_password.text)
        print(error_wrong_password.text)

    def tearDown(self):
        BaseTest.tearDown(self)
