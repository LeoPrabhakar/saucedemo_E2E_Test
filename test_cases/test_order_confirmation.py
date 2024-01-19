# Approach 1:-

import time
import pytest
from Saucedemo_new_E2E_test.page_objects.login_page import LoginPage
from Saucedemo_new_E2E_test.page_objects.plp_page import PLPPage
from Saucedemo_new_E2E_test.page_objects.pdp_page import PDPPage
from Saucedemo_new_E2E_test.page_objects.cart_page import CartPage
from Saucedemo_new_E2E_test.page_objects.checkout_page import CheckoutPage
from Saucedemo_new_E2E_test.page_objects.order_confirmation_page import OrderConfirmation
from Saucedemo_new_E2E_test.utilities.read_properties import Read_Config_File
from Saucedemo_new_E2E_test.utilities.custom_logger import Log_Gen
from ddt import ddt, data, unpack , file_data


# @pytest.mark.usefixtures("setup")
# @ddt
class Test_006_order_confirmation:
    # Load configuration and set up test data
    baseURL = Read_Config_File.get_url()
    username = Read_Config_File.get_username()
    password = Read_Config_File.get_password()
    product_name = Read_Config_File.get_product_link_text()
    first_name = Read_Config_File.get_first_name()
    last_name = Read_Config_File.get_last_name()
    pin_code = Read_Config_File.get_pin_code()
    logger = Log_Gen.log_gen()

    # @data(("Sauce Labs Backpack",), ("Test.allTheThings() T-Shirt (Red)",))
    # @unpack
    # @file_data("../test_data/InputData.json")
    def test_order_confirmation(self, setup):
        try:
            # Initialize test setup
            self.logger.info("********** Test_006_order_confirmation test initiated **********")
            self.driver = setup
            self.driver.get(self.baseURL)

            # Login
            self.lp = LoginPage(self.driver)
            self.lp.login_cred(self.username, self.password)
            self.lp.click_login_button()
            self.logger.info("********** Login is completed **********")

            # Navigate to specific product on PLP page
            self.logger.info("********** Verifying clicking on specific product on PLP page **********")
            self.plp = PLPPage(self.driver)
            self.plp.click_specific_product(self.product_name)
            # self.plp.click_specific_product(product_name)
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
            self.checkout.enter_user_info(self.first_name, self.last_name, self.pin_code)
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
            self.driver.quit()



#---------------------------------------------------------------------------------------------------------------

# Approach 2:-

# import time
# from Saucedemo_new_E2E_test.page_objects import login_page, plp_page, pdp_page, cart_page, checkout_page, order_confirmation
# from Saucedemo_new_E2E_test.utilities import read_properties, custom_logger
#
# class Test_006_order_confirmation:
#     baseURL, username, password, product_name, first_name, last_name, pin_code = (
#         read_properties.Read_Config_File.get_url(),
#         read_properties.Read_Config_File.get_username(),
#         read_properties.Read_Config_File.get_password(),
#         read_properties.Read_Config_File.get_product_link_text(),
#         read_properties.Read_Config_File.get_first_name(),
#         read_properties.Read_Config_File.get_last_name(),
#         read_properties.Read_Config_File.get_pin_code()
#     )
#     logger = custom_logger.Log_Gen.log_gen()
#
#     def test_order_confirmation(self, setup):
#         try:
#             self.logger.info("********** Test_006_order_confirmation test initiated **********")
#             self.driver = setup
#             self.driver.get(self.baseURL)
#
#             self.lp = login_page.LoginPage(self.driver)
#             self.lp.login_cred(self.username, self.password)
#             self.lp.click_login_button()
#             self.logger.info("********** Login is completed **********")
#
#             self.logger.info("********** Verifying clicking on specific product on PLP page **********")
#             self.plp = plp_page.PLPPage(self.driver)
#             for product_list in self.plp.get_product_link_text_elements():
#                 if self.product_name in product_list.text:
#                     product_list.click()
#                     break
#             self.logger.info("********** Specific product on PLP page is clicked and navigated to PDP**********")
#
#             self.logger.info("********** Clicking on Add to Cart button on PDP page**********")
#             self.pdp = pdp_page.PDPPage(self.driver)
#             self.pdp.click_add_to_cart_button()
#             self.pdp.click_cart_button()
#             self.logger.info("********** Clicked on Add to Cart button and navigated to cart page**********")
#
#             self.logger.info("********** Clicking on checkout button on cart page**********")
#             self.cart = cart_page.CartPage(self.driver)
#             self.cart.click_checkout_button()
#             self.logger.info("********** Clicked on checkout button and navigated to Checkout Page **********")
#
#             self.logger.info("********** Clicking on continue button on checkout page**********")
#             self.checkout = checkout_page.CheckoutPage(self.driver)
#             self.checkout.enter_user_info(self.first_name, self.last_name, self.pin_code)
#             self.checkout.click_continue_button()
#             self.logger.info("********** Clicked on checkout button and navigated to order confirmation Page **********")
#
#             self.logger.info("********** Clicking on finish and back to home button on confirmation page**********")
#             self.order_confirm = order_confirmation.OrderConfirmation(self.driver)
#             self.order_confirm.click_finish_button()
#             self.order_confirm.click_back_to_home_button()
#             self.logger.info("********** Clicked and navigated to home page **********")
#
#             self.logger.info("********* clicking on logout button *********")
#             self.lp.click_burger_menu_button()
#             time.sleep(2)
#             self.lp.click_logout_button()
#             self.logger.info("********* successfully logged out *********")
#             self.logger.info("******************** E2E testing completed ********************")
#
#         finally:
#             self.driver.close()
