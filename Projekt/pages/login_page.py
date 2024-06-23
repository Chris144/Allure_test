from Projekt.pages.home_page import BasePage
from Projekt.locators.locators import AccountLocators


class LoginPage(BasePage):

    def enter_email(self, email):
        # Enter the email
        self.driver.find_element(*AccountLocators.LOGIN_EMAIL).send_keys(email)

    def enter_password(self, password):
        # Enter the password
        self.driver.find_element(*AccountLocators.LOGIN_PASSWORD).send_keys(password)

    def click_login_button(self):
        # Click the button
        self.driver.find_element(*AccountLocators.LOGIN_BUTTON).click()
