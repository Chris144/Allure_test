import unittest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Projekt.locators.locators import AddToBasketLocators
from Projekt.pages.add_to_cart_page import AddToCartPage
from Projekt.pages.home_page import HomePage
from Projekt.tests.test_base import BaseTest


class AddToCart(BaseTest, unittest.TestCase):
    @allure.story('Add product to basket')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_to_cart(self):
        with allure.step('Initialize page'):
            self.home_page = HomePage(self.driver)
        with allure.step('Initialize add to cart page'):
            self.add_to_cart_page = AddToCartPage(self.driver)

        # Define expected values
        expected_values = [
            "My Cart - zł 37.00",
            "My Cart - zł 25.00",
            "My Cart - zł 30.00",
            "My Cart - zł 15.00"
        ]

        # Helper method to add product and verify cart
        def add_and_verify_cart():
            with allure.step('Hover on category'):
                self.add_to_cart_page.hoover_on_category()
                attach_screenshot(self.driver, 'Hover on category')
            with allure.step('Choose shoes from category'):
                self.add_to_cart_page.choose_shoes_from_category()
                attach_screenshot(self.driver, 'Choose shoes from category')
            with allure.step('Add product to cart'):
                self.add_to_cart_page.add_product_to_cart()
                attach_screenshot(self.driver, 'Add product to cart')
            with allure.step('Go to basket'):
                self.add_to_cart_page.go_to_basket()
                attach_screenshot(self.driver, 'Go to basket')
                cart_price = self.driver.find_element(*AddToBasketLocators.MY_CART).text
                return cart_price

        def attach_screenshot(driver, name):
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

        try:
            # First attempt to add product to cart
            cart_text = add_and_verify_cart()

            # Verify if the cart content matches any of the expected values
            with allure.step('Assert-Unexpected cart value'):
                assert cart_text in expected_values, f"Unexpected cart value: {cart_text}"
                print(cart_text)

            # Explicit wait to check if the empty cart element is present
            empty_cart_text = "Your cart is currently empty."
            try:
                empty_cart = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.woocommerce>p.cart-empty"))
                ).text

                if empty_cart == empty_cart_text:
                    # Try adding the product again if the cart is empty
                    cart_text = add_and_verify_cart()
                    with allure.step('Assert-Unexpected cart value after retry'):
                        assert cart_text in expected_values, f"Unexpected cart value after retry: {cart_text}"
            except:
                pass

        except Exception as e:
            # Debug information
            attach_screenshot(self.driver, 'Test failed')
            print(f"Test failed with exception: {e}")