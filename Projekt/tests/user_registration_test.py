import time
import unittest

from selenium.webdriver.common.by import By
from Projekt.pages.home_page import HomePage
from Projekt.pages.registration_page import RegistrationPage
from Projekt.tests.test_base import BaseTest
from Projekt.locators.locators import AccountLocators
from Projekt.test_data.data_faker_for_tests import AccountData


class RegistrationTest(BaseTest, unittest.TestCase):
    """
        Test checking user registration in various ways
    """

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.registration_page = RegistrationPage(self.driver)
        self.faker_data = AccountData()

    def test_registration_positive(self):
        """
        TC 001: Test checking user registration - positive
        """
        self.home_page.click_account()
        self.registration_page.enter_email(self.faker_data.registration_email)
        self.registration_page.enter_password(self.faker_data.registration_password)
        time.sleep(2)
        self.driver.find_element(*AccountLocators.REGISTER_OUT_CLICK_TO_ACTIVE).click()
        self.registration_page.click_registration_button()
        self.home_page.screenshot()
        positive_registration = self.driver.find_element(*AccountLocators.REGISTRATION_POSITIVE)
        error_no_registered_username = self.driver.find_element(*AccountLocators.REGISTRATION_POSITIVE_USERNAME)
        self.assertEqual(
            f"Hello {error_no_registered_username.text} (not {error_no_registered_username.text}? Log out)",
            positive_registration.text)
        print(positive_registration.text)

    def test_registration_no_email(self):
        """
        TC 002: Test checking user registration - no email
        """
        self.home_page.click_account()
        self.registration_page.enter_email('')
        self.registration_page.enter_password(self.faker_data.registration_password)
        time.sleep(2)
        self.driver.find_element(*AccountLocators.REGISTER_OUT_CLICK_TO_ACTIVE).click()
        self.registration_page.click_registration_button()
        self.home_page.screenshot()
        # Checking the expected effect using assert
        error_mail = self.driver.find_element(*AccountLocators.ASSERT_REGISTRATION_AND_LOGIN)
        self.assertEqual("Error: Please provide a valid email address.", error_mail.text)
        print(error_mail.text)

    def test_registration_no_password(self):
        """
        TC 003: Test checking user registration - no password
        """
        self.home_page.click_account()
        self.registration_page.enter_email(self.faker_data.registration_email)
        self.registration_page.enter_password('')
        self.registration_page.click_registration_button()
        self.home_page.screenshot()
        # Checking the expected effect using assert
        error_password = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        self.assertEqual("Error: Please enter an account password.", error_password.text)
        print(error_password.text)

    def test_registration_invalid_email(self):
        """
            TC 004: Test checking user registration - invalid email
        """
        self.home_page.click_account()
        self.registration_page.enter_email("jwdawd34452@dd")
        self.registration_page.enter_password('123123qewE43@@[]$23')
        time.sleep(2)
        self.registration_page.register_out_click_to_active_field()
        self.registration_page.click_registration_button()
        self.home_page.screenshot()
        # Checking the expected effect using assert
        error_mail = self.driver.find_element(By.CLASS_NAME, 'woocommerce-error')
        self.assertEqual("Error: Please provide a valid email address.", error_mail.text)
        print(error_mail.text)

    def test_registration_button_enabled_or_disabled(self):
        """
        TC 005: A test checking if the button is active or not depending on strength password
            1. Very_Week_Password - Button register should be Disabled
            2. Week_Password - Button register should be Disabled
            3. Medium - Button register should be Enabled
            4. Strong - Button register should be Enabled
        """

        def test_password(password, expected_results, message):
            self.registration_page.enter_password(password)
            self.registration_page.register_out_click_to_active_field()
            time.sleep(2)
            self.home_page.screenshot()
            self.assertEqual(self.registration_page.is_registration_button_enabled(), expected_results, message)
            print("For " + password + " expected_results should be :" + expected_results.__str__())

        self.home_page.click_account()
        # Very week password
        test_password("123", False, "Registration button should be disabled for very weak password")
        # Weak Password
        test_password("123pass", False, "Registration button should be disabled for weak password")
        # Medium Password
        test_password("123passPP23", True, "Registration button should be enabled for medium password")
        # Strong Password
        test_password("123passPP23@#[]444AS", True, "Registration button should be enabled for strong password")

    def tearDown(self):
        BaseTest.tearDown(self)
