from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import BillingDetailsLocators
from pages.base_page import BasePage


class BillingDetailsPage(BasePage):
    def proceed_to_checkout(self):
        # Click button "Proceed to checkout"
        self.driver.find_element(*BillingDetailsLocators.PROCEED_TO_CHECKOUT).click()

    def enter_first_name(self, first_name):
        # Enter first name
        self.driver.find_element(*BillingDetailsLocators.FIRST_NAME_BILLING).send_keys(first_name)

    def enter_last_name(self, last_name):
        # Enter last name
        self.driver.find_element(*BillingDetailsLocators.LAST_NAME_BILLING).send_keys(last_name)

    def enter_company_name(self, company_name):
        # Enter company name
        self.driver.find_element(*BillingDetailsLocators.COMPANY_NAME_BILLING).send_keys(company_name)

    def choose_country(self, country):
        # Locate the country dropdown element
        self.driver.find_element(*BillingDetailsLocators.COUNTRY_BILLING).click()
        i = self.driver.find_element(By.CLASS_NAME, 'select2-search__field')
        i.send_keys(country)
        self.driver.find_element(By.CLASS_NAME, 'select2-results').click()
        self.driver.find_element(*BillingDetailsLocators.STREET_ADDRESS_BILLING).click()

    def enter_state_county(self, state_county):
        # Enter the state county
        self.driver.find_element(*BillingDetailsLocators.STATE_COUNTY).send_keys(state_county)

    def enter_street_address(self, street_address):
        # Enter the street address
        self.driver.find_element(*BillingDetailsLocators.STREET_ADDRESS_BILLING).send_keys(street_address)

    def enter_address_optional(self, optional_address):
        # Enter the address in the optional field
        self.driver.find_element(*BillingDetailsLocators.ADDRESS_BILLING_OPTIONAL).send_keys(optional_address)

    def enter_postcode(self, postcode):
        # Enter the postcode
        self.driver.find_element(*BillingDetailsLocators.POSTCODE_ZIP_BILLING).send_keys(postcode)

    def enter_town_city(self, town_city):
        # Enter town or city
        self.driver.find_element(*BillingDetailsLocators.TOWN_CITY_BILLING).send_keys(town_city)

    def enter_phone(self, phone):
        # Enter phone number
        self.driver.find_element(*BillingDetailsLocators.PHONE_BILLING).send_keys(phone)

    def enter_email_address(self, email_address):
        # Enter email address
        self.driver.find_element(*BillingDetailsLocators.EMAIL_ADDRESS_BILLING).send_keys(email_address)

    def wait_for_invisibility(self):
        # Waiting for invisibility of the loader on the page
        try:
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element((By.CLASS_NAME, 'blockUI blockOverly'))
            )
        except TimeoutException:
            print("Timeout waiting for the loader to disappear.")

    def click_place_order(self):
        self.wait_for_invisibility()
        # CLick button "Place order"
        self.driver.find_element(*BillingDetailsLocators.PLACE_ORDER).click()

    def full_page_screenshot(self):
        self.wait_for_invisibility()
        screen_data = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        self.driver.save_screenshot(f"../screen_tests/billing-{screen_data}.png")
