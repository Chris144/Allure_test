from Projekt.pages.base_page import BasePage
from Projekt.locators.locators import AccountLocators


class RegistrationPage(BasePage):

    def enter_email(self, email):
        # Enter the email
        self.driver.find_element(*AccountLocators.REGISTER_EMAIL).send_keys(email)

    def enter_password(self, password):
        # Enter the password
        self.driver.find_element(*AccountLocators.REGISTER_PASSWORD).send_keys(password)

    def click_registration_button(self):
        # Click the button
        self.driver.find_element(*AccountLocators.REGISTER_BUTTON).click()

    def register_out_click_to_active_field(self):
        # Clicks on the element identified by "REGISTER_OUT_CLICK_TO_ACTIVE" to activate the field.
        self.driver.find_element(*AccountLocators.REGISTER_OUT_CLICK_TO_ACTIVE).click()

    def is_registration_button_enabled(self):
        registration_button = self.driver.find_element(*AccountLocators.REGISTER_BUTTON)
        return registration_button.is_enabled()
