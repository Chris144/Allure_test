from selenium.webdriver.common.by import By


class AccountLocators:
    # Registration locators
    ACCOUNT_LOCATOR = (By.CLASS_NAME, 'top-account')
    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BUTTON = (By.XPATH, '//input[@name="register"]')
    REGISTER_OUT_CLICK_TO_ACTIVE = (By.XPATH, '//label[@for="reg_password"]')
    STRONG_OF_PASSWORD = (By.XPATH, '//div[@aria-live="polite"]')
    LOGIN_EMAIL = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[value=Login]')
    LOGIN_REMEMBER_ME = (By.ID, 'rememberme')
    ASSERT_REGISTRATION_AND_LOGIN = (By.CLASS_NAME, 'woocommerce-error')
    ASSERT_REGISTRATION_NO_REGISTERED_USERNAME = (By.CSS_SELECTOR, 'div.woocommerce>ul>li>strong:last-child')
    LOGIN_POSITIVE_USERNAME = (By.CSS_SELECTOR, 'div.woocommerce-MyAccount-content>p:first-child')
    LOGIN_ERROR_USERNAME = (By.CLASS_NAME, 'woocommerce-error>li>strong:nth-child(2)')
    REGISTRATION_ERROR_USERNAME_PASSWORD = (By.CLASS_NAME, 'woocommerce-error>li>strong:nth-child(2)')
    REGISTRATION_POSITIVE = (By.CSS_SELECTOR, 'div.woocommerce-MyAccount-content>p:nth-child(1)')
    REGISTRATION_POSITIVE_USERNAME = (By.CSS_SELECTOR, 'div.woocommerce-MyAccount-content>p>strong:first-child')


class SortLocators:
    # Sorting locators
    MENU_ITEM = (By.ID, 'menu-item-128')
    ORDER_BY = (By.CLASS_NAME, 'orderby')
    FORM = (By.CLASS_NAME, 'woocommerce-ordering')
    OPTION_POPULARITY = (By.CSS_SELECTOR, 'select.orderby>option:nth-child(2)')
    OPTION_NEWNESS = (By.CSS_SELECTOR, 'select.orderby>option:nth-child(4)')
    OPTION_AVERAGE = (By.CSS_SELECTOR, 'select.orderby>option:nth-child(3)')


class AddToBasketLocators:
    # Add to basket locators
    MENU_ITEM_CATEGORIES = (By.ID, 'menu-item-123')
    DROP_DOWN_SHOES = (By.XPATH, "//a[@title='Shoes']")
    ADD_TO_CART = (By.CSS_SELECTOR, 'ul.products li.product>a.add_to_cart_button')
    MY_CART = (By.CLASS_NAME, 'top-cart')
    EMPTY_CART = (By.CSS_SELECTOR, 'div.woocommerce>p.cart-empty')


class BillingDetailsLocators:
    # Billing fill details locators
    PROCEED_TO_CHECKOUT = (By.CLASS_NAME, 'wc-proceed-to-checkout')
    FIRST_NAME_BILLING = (By.ID, 'billing_first_name')
    LAST_NAME_BILLING = (By.ID, 'billing_last_name')
    COMPANY_NAME_BILLING = (By.ID, 'billing_company')
    COUNTRY_BILLING = (By.ID, 'select2-billing_country-container')
    COUNTRY_BILLING_TEXT = (By.CLASS_NAME, 'select2-search__field')
    COUNTRY_BILLING_CHOOSE = (By.CSS_SELECTOR, 'ul.select2-results__options>li')
    STREET_ADDRESS_BILLING = (By.ID, 'billing_address_1')
    STATE_COUNTY = (By.ID, 'billing_state')
    ADDRESS_BILLING_OPTIONAL = (By.ID, 'billing_address_2')
    TOWN_CITY_BILLING = (By.ID, 'billing_city')
    POSTCODE_ZIP_BILLING = (By.ID, 'billing_postcode')
    PHONE_BILLING = (By.ID, 'billing_phone')
    EMAIL_ADDRESS_BILLING = (By.ID, 'billing_email')
    PLACE_ORDER = (By.ID, 'place_order')
    LIST_OF_ERRORS = (By.CLASS_NAME, 'woocommerce-error')
    ORDER = (By.CSS_SELECTOR, 'div.woocommerce-order>p')
