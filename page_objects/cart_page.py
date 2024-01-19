from selenium.webdriver.common.by import By


class CartPage:
    # XPath's locators for elements on the cart page
    REMOVE_BUTTON_XPATH = "//button[@class='btn btn_secondary btn_small cart_button']"
    CHECKOUT_BUTTON_XPATH = "//button[@id='checkout']"
    CONTINUE_SHOPPING_LINK_XPATH = "//button[@id='continue-shopping']"

    def __init__(self, driver):
        """
        Constructor for the CartPage class.
        :param driver: The WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def click_remove_button(self):
        """
        Clicks the 'Remove' button on the cart page.
        """
        self.driver.find_element(By.XPATH, self.REMOVE_BUTTON_XPATH).click()

    def click_checkout_button(self):
        """
        Clicks the 'Checkout' button on the cart page.
        """
        self.driver.find_element(By.XPATH, self.CHECKOUT_BUTTON_XPATH).click()

    def click_continue_shopping_link(self):
        """
        Clicks the 'Continue Shopping' link on the cart page.
        """
        self.driver.find_element(By.XPATH, self.CONTINUE_SHOPPING_LINK_XPATH).click()
