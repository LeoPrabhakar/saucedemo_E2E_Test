from selenium.webdriver.common.by import By

class PDPPage:
    # XPath locators for elements on the product details page (PDP)
    ADD_TO_CART_BUTTON_XPATH = "//button[@class='btn btn_primary btn_small btn_inventory']"
    BACK_TO_PLP_LINK_XPATH = "//button[@id='back-to-products']"
    CART_BUTTON_XPATH = "//a[@class='shopping_cart_link']"

    def __init__(self, driver):
        """
        Constructor for the PDPPage class.
        :param driver: The WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def click_add_to_cart_button(self):
        """
        Clicks the 'Add to Cart' button on the product details page.
        """
        self.driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_XPATH).click()

    def click_back_to_plp_link(self):
        """
        Clicks the 'Back to Products' link on the product details page.
        """
        self.driver.find_element(By.XPATH, self.BACK_TO_PLP_LINK_XPATH).click()

    def click_cart_button(self):
        """
        Clicks the 'Cart' button on the product details page.
        """
        self.driver.find_element(By.XPATH, self.CART_BUTTON_XPATH).click()
