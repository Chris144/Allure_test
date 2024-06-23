import unittest

import allure

from Projekt.locators.locators import BillingDetailsLocators
from Projekt.pages.add_to_cart_page import AddToCartPage
from Projekt.pages.billing_details_page import BillingDetailsPage
from Projekt.pages.home_page import HomePage
from Projekt.test_data.data_faker_for_tests import BillingData
from Projekt.tests.add_to_cart_test import AddToCart


class BillingDetails(AddToCart, unittest.TestCase):

    def setUp(self):
        super().setUp()
        with allure.step('Initialize page'):
            self.home_page = HomePage(self.driver)
            self.add_to_cart_page = AddToCartPage(self.driver)
            self.billing_details = BillingDetailsPage(self.driver)
            self.faker_data = BillingData()
            self.driver.implicitly_wait(10)

    @allure.story('Fill billing details')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_positive_place_order(self):
        """
            TC 001: Test checking positive fill:
        """
        # Calling the add to cart method
        with allure.step('Add product to cart'):
            self.test_add_to_cart()
        with allure.step('Proceed_to_checkout'):
            self.billing_details.proceed_to_checkout()
        with allure.step('Enter_first_name'):
            self.billing_details.enter_first_name(BillingData.first_name)
        with allure.step('Enter_last_name'):
            self.billing_details.enter_last_name(BillingData.last_name)
        with allure.step('Enter_company_name'):
            self.billing_details.enter_company_name(BillingData.company)
        with allure.step('Enter_choose_country'):
            self.billing_details.choose_country('Poland')
        with allure.step('Enter_street_address'):
            self.billing_details.enter_street_address(BillingData.street_address)
        with allure.step('Enter_address_optional'):
            self.billing_details.enter_address_optional(BillingData.street_address_optional)
        with allure.step('Enter_postcode'):
            self.billing_details.enter_postcode(BillingData.post_code)
        with allure.step('Enter_town_city'):
            self.billing_details.enter_town_city(BillingData.town_city)
        with allure.step('Enter_phone'):
            self.billing_details.enter_phone(BillingData.phone)
        with allure.step('Enter_email_address'):
            self.billing_details.enter_email_address(BillingData.email)
        with allure.step('Click_place_order'):
            self.billing_details.click_place_order()
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='Add product to cart')
        with allure.step('Checking assert'):
            order = self.driver.find_element(*BillingDetailsLocators.ORDER)
            self.assertEqual("Thank you. Your order has been received.", order.text)
            print(order.text)

    def test_no_enter_first_name(self):
        """
            TC 002: Test - no first name:
        """
        # Calling the add to cart method
        with allure.step('Add product to cart'):
            self.test_add_to_cart()
        with allure.step('Proceed_to_checkout'):
            self.billing_details.proceed_to_checkout()
        with allure.step('No_enter_first_name'):
            self.billing_details.enter_first_name('')
        with allure.step('Enter_last_name'):
            self.billing_details.enter_last_name(BillingData.last_name)
        with allure.step('Enter_company_name'):
            self.billing_details.enter_company_name(BillingData.company)
        with allure.step('Enter_choose_country'):
            self.billing_details.choose_country('Poland')
        with allure.step('Enter_street_address'):
            self.billing_details.enter_street_address(BillingData.street_address)
        with allure.step('Enter_address_optional'):
            self.billing_details.enter_address_optional(BillingData.street_address_optional)
        with allure.step('Enter_postcode'):
            self.billing_details.enter_postcode(BillingData.post_code)
        with allure.step('Enter_town_city'):
            self.billing_details.enter_town_city(BillingData.town_city)
        with allure.step('Enter_phone'):
            self.billing_details.enter_phone(BillingData.phone)
        with allure.step('Enter_email_address'):
            self.billing_details.enter_email_address(BillingData.email)
        with allure.step('Click_place_order'):
            self.billing_details.click_place_order()
        with allure.step('Taking_screenshot'):
            self.base_page.attach_screenshot(name='Add product to cart')
        with allure.step('Checking assert'):
            lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
            self.assertEqual("Billing First name is a required field.", lista_errors.text)
            print(lista_errors.text)

    def test_no_enter_last_name(self):
        """
            TC 003: Test - no last name:
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name('')
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Poland')
        self.billing_details.enter_street_address(BillingData.street_address)
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode(BillingData.post_code)
        self.billing_details.enter_town_city(BillingData.town_city)
        self.billing_details.enter_phone(BillingData.phone)
        self.billing_details.enter_email_address(BillingData.email)
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Billing Last name is a required field.",
                         lista_errors.text)
        print(lista_errors.text)

    def test_no_selecting_country(self):
        """
            TC 003: Test - no country:
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name(BillingData.last_name)
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Select a country…')
        self.billing_details.enter_street_address(BillingData.street_address)
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode(BillingData.post_code)
        self.billing_details.enter_state_county(BillingData.state_county)
        self.billing_details.enter_town_city(BillingData.town_city)
        self.billing_details.enter_phone(BillingData.phone)
        self.billing_details.enter_email_address(BillingData.email)
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Billing Country is a required field.\nPlease enter an address to continue.",
                         lista_errors.text)
        print(lista_errors.text)

    def test_no_enter_street_address(self):
        """
            TC 004: Test - no street address
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name(BillingData.last_name)
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Poland')
        self.billing_details.enter_street_address('')
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode(BillingData.post_code)
        self.billing_details.enter_town_city(BillingData.town_city)
        self.billing_details.enter_phone(BillingData.phone)
        self.billing_details.enter_email_address(BillingData.email)
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Billing Street address is a required field.", lista_errors.text)
        print(lista_errors.text)

    def test_no_enter_postcode(self):
        """
            TC 005: Test - no postcode
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name(BillingData.last_name)
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Poland')
        self.billing_details.enter_street_address(BillingData.street_address)
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode('')
        self.billing_details.enter_town_city(BillingData.town_city)
        self.billing_details.enter_phone(BillingData.phone)
        self.billing_details.enter_email_address(BillingData.email)
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Please enter a valid postcode / ZIP.", lista_errors.text)
        print(lista_errors.text)

    def test_no_enter_town_city(self):
        """
            TC 006: Test - no town or city:
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name(BillingData.last_name)
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Poland')
        self.billing_details.enter_street_address(BillingData.street_address)
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode(BillingData.post_code)
        self.billing_details.enter_town_city('')
        self.billing_details.enter_phone(BillingData.phone)
        self.billing_details.enter_email_address(BillingData.email)
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Billing Town / City is a required field.", lista_errors.text)
        print(lista_errors.text)

    def test_no_enter_phone(self):
        """
            TC 007: Test - no phone:
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name(BillingData.last_name)
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Poland')
        self.billing_details.enter_street_address(BillingData.street_address)
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode(BillingData.post_code)
        self.billing_details.enter_town_city(BillingData.town_city)
        self.billing_details.enter_phone('')
        self.billing_details.enter_email_address(BillingData.email)
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Billing Phone is a required field.", lista_errors.text)
        print(lista_errors.text)

    def test_no_email_address(self):
        """
            TC 008: Test - no email address:
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name(BillingData.last_name)
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Poland')
        self.billing_details.enter_street_address(BillingData.street_address)
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode(BillingData.post_code)
        self.billing_details.enter_town_city(BillingData.town_city)
        self.billing_details.enter_phone(BillingData.phone)
        self.billing_details.enter_email_address('')
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Billing Email address is a required field.", lista_errors.text)
        print(lista_errors.text)

    def test_incorrect_phone_number(self):
        """
            TC 009: Test - incorrect phone number
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name(BillingData.last_name)
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Poland')
        self.billing_details.enter_street_address(BillingData.street_address)
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode(BillingData.post_code)
        self.billing_details.enter_town_city(BillingData.town_city)
        self.billing_details.enter_phone('XRETW')
        self.billing_details.enter_email_address(BillingData.email)
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Billing Phone is not a valid phone number.", lista_errors.text)
        print(lista_errors.text)

    def test_incorrect_email_address(self):
        """
            TC 010: Test - incorrect email address
        """
        # Calling the add to cart method
        self.test_add_to_cart()
        self.billing_details.proceed_to_checkout()
        self.billing_details.enter_first_name(BillingData.first_name)
        self.billing_details.enter_last_name(BillingData.last_name)
        self.billing_details.enter_company_name(BillingData.company)
        self.billing_details.choose_country('Poland')
        self.billing_details.enter_street_address(BillingData.street_address)
        self.billing_details.enter_address_optional(BillingData.street_address_optional)
        self.billing_details.enter_postcode(BillingData.post_code)
        self.billing_details.enter_town_city(BillingData.town_city)
        self.billing_details.enter_phone(BillingData.phone)
        self.billing_details.enter_email_address('joanna@s')
        self.billing_details.click_place_order()
        self.billing_details.full_page_screenshot()
        lista_errors = self.driver.find_element(*BillingDetailsLocators.LIST_OF_ERRORS)
        self.assertEqual("Billing Email address is not a valid email address.", lista_errors.text)
        print(lista_errors.text)

    def tearDown(self):
        self.driver.quit()
