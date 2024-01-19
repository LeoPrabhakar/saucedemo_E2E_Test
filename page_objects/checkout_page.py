from selenium.webdriver.common.by import By


class CheckoutPage:
    # XPath's locators for elements on the checkout page
    FIRST_NAME_XPATH = "//input[@id='first-name']"
    LAST_NAME_XPATH = "//input[@id='last-name']"
    PIN_CODE_XPATH = "//input[@id='postal-code']"
    CONTINUE_BUTTON_XPATH = "//input[@id='continue']"
    CANCEL_BUTTON_XPATH = "//button[@id='cancel']"

    def __init__(self, driver):
        """
        Constructor for the CheckoutPage class.
        :param driver: The WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def enter_first_name(self, first_name):
        """
        Enters the first name in the corresponding input field on the checkout page.
        :param first_name: The first name to be entered.
        """
        self.driver.find_element(By.XPATH, self.FIRST_NAME_XPATH).send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        Enters the last name in the corresponding input field on the checkout page.
        :param last_name: The last name to be entered.
        """
        self.driver.find_element(By.XPATH, self.LAST_NAME_XPATH).send_keys(last_name)

    def enter_pin_code(self, pin_code):
        """
        Enters the PIN code in the corresponding input field on the checkout page.
        :param pin_code: The PIN code to be entered.
        """
        self.driver.find_element(By.XPATH, self.PIN_CODE_XPATH).send_keys(pin_code)

    def click_continue_button(self):
        """
        Clicks the 'Continue' button on the checkout page.
        """
        self.driver.find_element(By.XPATH, self.CONTINUE_BUTTON_XPATH).click()

    def click_cancel_button(self):
        """
        Clicks the 'Cancel' button on the checkout page.
        """
        self.driver.find_element(By.XPATH, self.CANCEL_BUTTON_XPATH).click()

    def enter_user_info(self, first_name, last_name, pin_code):
        """
        Enters user information (first name, last name, and PIN code) on the checkout page.
        :param first_name: The first name to be entered.
        :param last_name: The last name to be entered.
        :param pin_code: The PIN code to be entered.
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_pin_code(pin_code)
