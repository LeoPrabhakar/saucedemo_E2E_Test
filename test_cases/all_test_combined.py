# this is used to validate hooks and markers

import time
import pytest
from selenium.webdriver.common.by import By
from Saucedemo_new_E2E_test.page_objects.login_page import LoginPage
from Saucedemo_new_E2E_test.page_objects.plp_page import PLPPage
from Saucedemo_new_E2E_test.page_objects.pdp_page import PDPPage
from Saucedemo_new_E2E_test.page_objects.cart_page import CartPage
from Saucedemo_new_E2E_test.page_objects.checkout_page import CheckoutPage
from Saucedemo_new_E2E_test.page_objects.order_confirmation_page import OrderConfirmation
from Saucedemo_new_E2E_test.utilities.read_properties import Read_Config_File
from Saucedemo_new_E2E_test.utilities.custom_logger import Log_Gen


# Define a test class for all test cases
class Test_001_Login:
    # Load configuration and set up test data
    baseURL = Read_Config_File.get_url()
    username = Read_Config_File.get_username()
    password = Read_Config_File.get_password()
    product_name = Read_Config_File.get_product_link_text()
    first_name = Read_Config_File.get_first_name()
    last_name = Read_Config_File.get_last_name()
    pin_code = Read_Config_File.get_pin_code()
    logger = Log_Gen.log_gen()

    # Test to verify the home page title
    @pytest.mark.skip
    def test_home_page_title(self, setup):
        self.logger.info("********** Verifying login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        # Check if the actual title matches the expected title
        if actual_title == "Swag Labs":
            assert True
            self.logger.info("********** Home page title is matched with expected title **********")
        else:
            assert False
            self.logger.info("********** Home page title is not matched with expected title **********")
        self.driver.close()

# ---------------------------------------------------------------------------------------------------------
    # Test to perform login and verify the Products page title
    @pytest.mark.xfail
    def test_login(self, setup):
        self.logger.info("********** Test_Login_001 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        # Input login credentials
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()
        # Verify the Products page title
        actual_title_element = self.driver.find_element(By.XPATH, "//span[@class='title']")
        actual_title = actual_title_element.text
        if actual_title == "Products":
            assert True
            self.logger.info("********** Products page title is matched with expected title **********")
        else:
            assert False
            self.logger.info("********** Products page title is not matched with expected title **********")
        # Perform logout
        self.lp.click_burger_menu_button()
        time.sleep(2)
        self.lp.click_logout_button()
        self.driver.close()

# ---------------------------------------------------------------------------------------------------------
    @pytest.mark.sanity
    def test_plp(self, setup):
        try:
            # Initialize test setup
            self.logger.info("********** Test_006_order_confirmation test initiated **********")
            self.driver = setup
            self.driver.get(self.baseURL)

            # Login
            self.lp = LoginPage(self.driver)
            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login_button()
            self.logger.info("********** Login is completed **********")

            # Navigate to specific product on PLP page
            self.logger.info("********** Verifying clicking on specific product on PLP page **********")
            self.plp = PLPPage(self.driver)
            product_lists = self.plp.get_product_link_text_elements()
            for product_list in product_lists:
                if self.product_name in product_list.text:
                    product_list.click()
                    break
            self.logger.info("********** Specific product on PLP page is clicked and navigated to PDP**********")
        finally:
            self.driver.close

# ---------------------------------------------------------------------------------------------------------
    @pytest.mark.regression
    def test_pdp(self, setup):
        try:
            # Initialize test setup
            self.logger.info("********** Test_006_order_confirmation test initiated **********")
            self.driver = setup
            self.driver.get(self.baseURL)

            # Login
            self.lp = LoginPage(self.driver)
            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login_button()
            self.logger.info("********** Login is completed **********")

            # Navigate to specific product on PLP page
            self.logger.info("********** Verifying clicking on specific product on PLP page **********")
            self.plp = PLPPage(self.driver)
            product_lists = self.plp.get_product_link_text_elements()
            for product_list in product_lists:
                if self.product_name in product_list.text:
                    product_list.click()
                    break
            self.logger.info("********** Specific product on PLP page is clicked and navigated to PDP**********")

            # Add to Cart on PDP page
            self.logger.info("********** Clicking on Add to Cart button on PDP page**********")
            self.pdp = PDPPage(self.driver)
            self.pdp.click_add_to_cart_button()
            self.pdp.click_cart_button()
            self.logger.info("********** Clicked on Add to Cart button and navigated to checkout page**********")
        finally:
            self.driver.close

# ---------------------------------------------------------------------------------------------------------
    @pytest.mark.regression
    def test_cart(self, setup):
        try:
            # Initialize test setup
            self.logger.info("********** Test_006_order_confirmation test initiated **********")
            self.driver = setup
            self.driver.get(self.baseURL)

            # Login
            self.lp = LoginPage(self.driver)
            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login_button()
            self.logger.info("********** Login is completed **********")

            # Navigate to specific product on PLP page
            self.logger.info("********** Verifying clicking on specific product on PLP page **********")
            self.plp = PLPPage(self.driver)
            product_lists = self.plp.get_product_link_text_elements()
            for product_list in product_lists:
                if self.product_name in product_list.text:
                    product_list.click()
                    break
            self.logger.info("********** Specific product on PLP page is clicked and navigated to PDP**********")

            # Add to Cart on PDP page
            self.logger.info("********** Clicking on Add to Cart button on PDP page**********")
            self.pdp = PDPPage(self.driver)
            self.pdp.click_add_to_cart_button()
            self.pdp.click_cart_button()
            self.logger.info("********** Clicked on Add to Cart button and navigated to checkout page**********")
        finally:
            self.driver.close

# ---------------------------------------------------------------------------------------------------------
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_checkout(self, setup):
        try:
            # Initialize test setup
            self.logger.info("********** Test_006_order_confirmation test initiated **********")
            self.driver = setup
            self.driver.get(self.baseURL)

            # Login
            self.lp = LoginPage(self.driver)
            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login_button()
            self.logger.info("********** Login is completed **********")

            # Navigate to specific product on PLP page
            self.logger.info("********** Verifying clicking on specific product on PLP page **********")
            self.plp = PLPPage(self.driver)
            product_lists = self.plp.get_product_link_text_elements()
            for product_list in product_lists:
                if self.product_name in product_list.text:
                    product_list.click()
                    break
            self.logger.info("********** Specific product on PLP page is clicked and navigated to PDP**********")

            # Add to Cart on PDP page
            self.logger.info("********** Clicking on Add to Cart button on PDP page**********")
            self.pdp = PDPPage(self.driver)
            self.pdp.click_add_to_cart_button()
            self.pdp.click_cart_button()
            self.logger.info("********** Clicked on Add to Cart button and navigated to checkout page**********")

            # Cart page
            self.logger.info("********** Clicking on checkout button on PDP page**********")
            self.cart = CartPage(self.driver)
            self.cart.click_checkout_button()
            self.logger.info("********** Clicked on checkout button and navigated to Checkout Page **********")

            # Continue with Checkout
            self.logger.info("********** Clicking on continue button on checkout page**********")
            self.checkout = CheckoutPage(self.driver)
            self.checkout.enter_first_name(self.first_name)
            self.checkout.enter_last_name(self.last_name)
            self.checkout.enter_pin_code(self.pin_code)
            self.checkout.click_continue_button()
            self.logger.info("********** Clicked on checkout button and navigated to order confirmation Page **********")
        finally:
            self.driver.close

# ---------------------------------------------------------------------------------------------------------
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_order_confirmation(self, setup):
        try:
            # Initialize test setup
            self.logger.info("********** Test_006_order_confirmation test initiated **********")
            self.driver = setup
            self.driver.get(self.baseURL)

            # Login
            self.lp = LoginPage(self.driver)
            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login_button()
            self.logger.info("********** Login is completed **********")

            # Navigate to specific product on PLP page
            self.logger.info("********** Verifying clicking on specific product on PLP page **********")
            self.plp = PLPPage(self.driver)
            product_lists = self.plp.get_product_link_text_elements()
            for product_list in product_lists:
                if self.product_name in product_list.text:
                    product_list.click()
                    break
            self.logger.info("********** Specific product on PLP page is clicked and navigated to PDP**********")

            # Add to Cart on PDP page
            self.logger.info("********** Clicking on Add to Cart button on PDP page**********")
            self.pdp = PDPPage(self.driver)
            self.pdp.click_add_to_cart_button()
            self.pdp.click_cart_button()
            self.logger.info("********** Clicked on Add to Cart button and navigated to cart page**********")

            # Cart page
            self.logger.info("********** Clicking on checkout button on cart page**********")
            self.cart = CartPage(self.driver)
            self.cart.click_checkout_button()
            self.logger.info("********** Clicked on checkout button and navigated to Checkout Page **********")

            # Continue with Checkout
            self.logger.info("********** Clicking on continue button on checkout page**********")
            self.checkout = CheckoutPage(self.driver)
            self.checkout.enter_first_name(self.first_name)
            self.checkout.enter_last_name(self.last_name)
            self.checkout.enter_pin_code(self.pin_code)
            self.checkout.click_continue_button()
            self.logger.info("********** Clicked on checkout button and navigated to order confirmation Page **********")

            # Order Confirmation
            self.logger.info("********** Clicking on finish and back to home button on confirmation page**********")
            self.order_confirm = OrderConfirmation(self.driver)
            self.order_confirm.click_finish_button()
            self.order_confirm.click_back_to_home_button()
            self.logger.info("********** Clicked and navigated to home page **********")

            # Logout
            self.logger.info("********* clicking on logout button *********")
            self.lp.click_burger_menu_button()
            time.sleep(2)
            self.lp.click_logout_button()
            self.logger.info("********* successfully logged out *********")
            self.logger.info("******************** E2E testing completed ********************")
        finally:
            self.driver.close

