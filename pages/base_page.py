import allure


class BasePage:
    """
    Base class for each Page
    """

    def __init__(self, driver):
        self.driver = driver

    def attach_screenshot(self, name):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
