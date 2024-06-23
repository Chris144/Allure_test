import random

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains

from Projekt.locators.locators import AddToBasketLocators
from Projekt.pages.base_page import BasePage


class AddToCartPage(BasePage):
    def hoover_on_category(self):
        # Checking whether the Hoover is visible when you hover the mouse over it
        element_to_account = self.driver.find_element(*AddToBasketLocators.MENU_ITEM_CATEGORIES)
        action = ActionChains(self.driver)
        action.move_to_element(element_to_account).perform()

    def choose_shoes_from_category(self):
        # Choosing category shoes from the menu
        self.driver.find_element(*AddToBasketLocators.DROP_DOWN_SHOES).click()

    def add_product_to_cart(self):
        try:
            # Finding all elements that can be added to the cart
            elements = self.driver.find_elements(*AddToBasketLocators.ADD_TO_CART)
            if elements:
                # Choose random element from list
                random_element = random.choice(elements)
                random_element.click()
            else:
                # Print a message if no products are found
                print("No products available to add to the cart.")
        except NoSuchElementException as e:
            # Exception handling when no element is found
            print(f"No such element: {str(e)}")
            self.driver.quit()

    def go_to_basket(self):
        # Go to cart
        self.driver.find_element(*AddToBasketLocators.MY_CART).click()
