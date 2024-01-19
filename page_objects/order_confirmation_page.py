from selenium.webdriver.common.by import By


class OrderConfirmation:
    # XPath's locators for elements on the order confirmation page
    FINISH_BUTTON_XPATH = "//button[@id='finish']"
    CANCEL_BUTTON_XPATH = "//button[@id='cancel']"
    BACK_TO_HOME_BUTTON_XPATH = "//button[@id='back-to-products']"

    def __init__(self, driver):
        """
        Constructor for the OrderConfirmation class.
        :param driver: The WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def click_finish_button(self):
        """
        Clicks the 'Finish' button on the order confirmation page.
        """
        self.driver.find_element(By.XPATH, self.FINISH_BUTTON_XPATH).click()

    def click_cancel_button(self):
        """
        Clicks the 'Cancel' button on the order confirmation page.
        """
        self.driver.find_element(By.XPATH, self.CANCEL_BUTTON_XPATH).click()

    def click_back_to_home_button(self):
        """
        Clicks the 'Back to Home' button on the order confirmation page.
        """
        self.driver.find_element(By.XPATH, self.BACK_TO_HOME_BUTTON_XPATH).click()


