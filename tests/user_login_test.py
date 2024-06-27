import allure

from locators.locators import AccountLocators
from pages.base_page import BasePage
from pages.home_page import HomePage

from pages.login_page import LoginPage
from test_data.data_faker_for_tests import AccountData
from ddt import ddt, data, unpack
from test_data.read_Data_from_excel import ReadFile
from test_base import BaseTest


@ddt
class TestLogin(BaseTest):
    """
        Test checking user logging in various ways
    """

    def setUp(self):
        with allure.step('Initialize page'):
            super().setUp()
            self.home_page = HomePage(self.driver)
            self.login_page = LoginPage(self.driver)
            self.faker_data = AccountData()
            self.base_page = BasePage(self.driver)

    @allure.story('Fill billing details')
    @allure.severity(allure.severity_level.CRITICAL)
    @data(ReadFile.get_test_data(0))
    @unpack
    def test_login_positive_enter_email(self, username_email, password):
        """
        TC 001: Test checking user login enter email - positive
        """
        with allure.step('Click_account'):
            self.home_page.click_account()
        with allure.step('Enter_email'):
            self.login_page.enter_email(username_email)
        with allure.step('Enter_password'):
            self.login_page.enter_password(password)
        with allure.step('Click_login_button'):
            self.login_page.click_login_button()
        with allure.step('Checking assert'):
            positive_login = self.driver.find_element(*AccountLocators.LOGIN_POSITIVE_USERNAME)
            self.assertEqual("Hello jaimechapman (not jaimechapman? Log out)", positive_login.text)
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='Login_positive_enter_email')

    @data(ReadFile.get_test_data(1))
    @unpack
    def test_login_positive_enter_username(self, username_email, password):
        """
        TC 002: Test checking user login enter username - positive
        """
        with allure.step('Click_account'):
            self.home_page.click_account()
        with allure.step('Enter_username'):
            self.login_page.enter_email(username_email)
        with allure.step('Enter_password'):
            self.login_page.enter_password(password)
        with allure.step('Click_login_button'):
            self.login_page.click_login_button()
        with allure.step('Checking assert'):
            positive_login = self.driver.find_element(*AccountLocators.LOGIN_POSITIVE_USERNAME)
            self.assertEqual("Hello jaimechapman (not jaimechapman? Log out)", positive_login.text)
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='login_positive_enter_username')

    @data(ReadFile.get_test_data(2))
    @unpack
    def test_login_no_email(self, username_email, password):
        """
        TC 003: Test checking user login - empty field email
        """
        with allure.step('Click_account'):
            self.home_page.click_account()
        with allure.step('Enter_username'):
            self.login_page.enter_email('')
        with allure.step('Enter_password'):
            self.login_page.enter_password(password)
        with allure.step('Click_login_button'):
            self.login_page.click_login_button()
        with allure.step('Checking assert'):
            error_mail = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
            self.assertEqual("Error: Username is required.", error_mail.text)
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='Login_no_email')

    @data(ReadFile.get_test_data(3))
    @unpack
    def test_login_no_password(self, username_email, password):
        """
        TC 004: Test checking user login - empty field password
        """
        with allure.step('Click_account'):
            self.home_page.click_account()
        with allure.step('Enter_username'):
            self.login_page.enter_email(username_email)
        with allure.step('No_enter_password'):
            self.login_page.enter_password('')
        with allure.step('Click_login_button'):
            self.login_page.click_login_button()
        with allure.step('Checking assert'):
            error_password = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
            self.assertEqual("Error: The password field is empty.", error_password.text)
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='Login_no_password')

    @data(ReadFile.get_test_data(4))
    @unpack
    def test_login_user_not_registered_enter_username(self, username_email, password):
        """
        TC 005: Test checking user is not registered
        """
        with allure.step('Click_account'):
            self.home_page.click_account()
        with allure.step('Enter_email'):
            self.login_page.enter_email(username_email)
        with allure.step('Enter_password'):
            self.login_page.enter_password(password)
        with allure.step('Click_login_button'):
            self.login_page.click_login_button()
        with allure.step('Checking assert'):
            error_no_registered = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
            error_no_registered_username = (self.driver.find_element
                                            (*AccountLocators.ASSERT_REGISTRATION_NO_REGISTERED_USERNAME))
            self.assertEqual(f"Error: The username {error_no_registered_username.text} is not registered on this site."
                             f" If you are unsure of your username, try your email address instead.",
                             error_no_registered.text)
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='Login_user_not_registered_enter_username')

    @data(ReadFile.get_test_data(5))
    @unpack
    def test_login_user_not_registered_enter_email(self, username_email, password):
        """
        TC 006: Test checking user is not registered
        """
        with allure.step('Click_account'):
            self.home_page.click_account()
        with allure.step('Enter_email'):
            self.login_page.enter_email(username_email)
        with allure.step('Enter_password'):
            self.login_page.enter_password(password)
        with allure.step('Click_login_button'):
            self.login_page.click_login_button()
        with allure.step('Checking assert'):
            error_no_registered = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
            self.assertEqual("Error: A user could not be found with this email address.", error_no_registered.text)
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='Login_user_not_registered_enter_email')

    @data(ReadFile.get_test_data(6))
    @unpack
    def test_login_incorrect_password(self, username_email, password):
        """
        TC007: Test checking user login - incorrect password
        """
        with allure.step('Click_account'):
            self.home_page.click_account()
        with allure.step('Enter_email'):
            self.login_page.enter_email(username_email)
        with allure.step('Enter_password'):
            self.login_page.enter_password(password)
        with allure.step('Click_login_button'):
            self.login_page.click_login_button()
        with allure.step('Checking assert'):
            error_wrong_password = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
            error_wrong_password_username = self.driver.find_element(*AccountLocators.LOGIN_ERROR_USERNAME)
            self.assertEqual(
                f"Error: The password you entered for the username {error_wrong_password_username.text} is incorrect."
                f" Lost your password?", error_wrong_password.text)
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='Login_incorrect_password')

    def tearDown(self):
        BaseTest.tearDown(self)
