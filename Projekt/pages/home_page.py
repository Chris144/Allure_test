from datetime import datetime

from selenium.webdriver import ActionChains

from Projekt.pages.base_page import BasePage
from Projekt.pages.login_page import LoginPage
from Projekt.pages.registration_page import RegistrationPage
from Projekt.locators.locators import AccountLocators, SortLocators
from Projekt.pages.sort_page import SortPage


class HomePage(BasePage):
    def click_account(self):
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        element_to_account.click()
        return LoginPage(self.driver), RegistrationPage(self.driver)

    def hoover_on_account(self):
        # Checking whether the Hoover is visible when you hover the mouse over it
        element_to_account = self.driver.find_element(*AccountLocators.ACCOUNT_LOCATOR)
        action = ActionChains(self.driver)
        action.move_to_element(element_to_account).perform()

    def screenshot(self):
        datetime.now()
        screenDatetime = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        self.driver.save_screenshot(f"../screen_tests/screenshot-{screenDatetime}.png")

    def choose_menu(self):
        # 2. Chose from menu
        self.driver.find_element(*SortLocators.MENU_ITEM).click()
        return SortPage(self.driver)
