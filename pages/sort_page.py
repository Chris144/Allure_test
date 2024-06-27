from selenium.webdriver.support.select import Select

from locators.locators import SortLocators
from pages.base_page import BasePage


class SortPage(BasePage):
    def click_on_sorting_list(self):
        # 3. Click an element to choose sorting
        form = self.driver.find_element(*SortLocators.FORM)
        form.click()

    def select_sorting_by_popularity(self):
        # Select sorting by popularity
        select = Select(self.driver.find_element(*SortLocators.ORDER_BY))
        select.select_by_value('popularity')

    def select_sorting_by_newness(self):
        # Select sorting by date
        select = Select(self.driver.find_element(*SortLocators.ORDER_BY))
        select.select_by_value('date')

    def select_sorting_by_average(self):
        # Select sorting by rating
        select = Select(self.driver.find_element(*SortLocators.ORDER_BY))
        select.select_by_value('rating')
