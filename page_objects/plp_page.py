from selenium import webdriver
from selenium.webdriver.common.by import By

class PLPPage:
    # XPath's locators for elements on the product list page (PLP)
    PRODUCT_LINK_TEXT_XPATH = "//div[@class='inventory_list']//div//div[2]//a//div"
    PRODUCT_LINK_IMAGE_XPATH = "//div[@class='inventory_list']//a//img"
    ADD_TO_CART_BUTTON_XPATH = '//button[@class="btn btn_primary btn_small btn_inventory "]'
    FILTER_DROPDOWN_XPATH = "//select[@class='product_sort_container']"
    FILTER_DROPDOWN_OPTIONS_XPATH = "//select//option"
    BURGER_MENU_BUTTON_XPATH = "//button[@id='react-burger-menu-btn']"
    LOGOUT_BUTTON_XPATH = "//nav[@class='bm-item-list']//a"

    def __init__(self, driver):
        """
        Constructor for the PLPPage class.
        :param driver: The WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def get_product_link_text_elements(self):
        """
        Finds and returns a list of elements representing product links' text on the product list page.
        :return: List of WebElement objects.
        """
        return self.driver.find_elements(By.XPATH, self.PRODUCT_LINK_TEXT_XPATH)

    def get_product_link_image_elements(self):
        """
        Finds and returns a list of elements representing product links' images on the product list page.
        :return: List of WebElement objects.
        """
        return self.driver.find_elements(By.XPATH, self.PRODUCT_LINK_IMAGE_XPATH)

    def get_plp_add_to_cart_button_elements(self):
        """
        Finds and returns a list of elements representing 'Add to Cart' buttons on the product list page.
        :return: List of WebElement objects.
        """
        return self.driver.find_elements(By.XPATH, self.ADD_TO_CART_BUTTON_XPATH)

    def click_specific_product(self, product_name):
        """
        Clicks on a specific product in the product list based on the provided product name.
        :param product_name: The name of the product to click.
        """
        product_lists = self.get_product_link_text_elements()
        for product_list in product_lists:
            if product_name in product_list.text:
                product_list.click()
                break

