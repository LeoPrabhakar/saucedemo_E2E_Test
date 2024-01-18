import time
from Saucedemo_new_E2E_test.page_objects.login_page import LoginPage
from Saucedemo_new_E2E_test.page_objects.plp_page import PLPPage
from Saucedemo_new_E2E_test.page_objects.pdp_page import PDPPage
from Saucedemo_new_E2E_test.utilities.read_properties import Read_Config_File
from Saucedemo_new_E2E_test.utilities.custom_logger import Log_Gen


class Test_003_pdp:
    # Load configuration and set up test data
    baseURL = Read_Config_File.get_url()
    username = Read_Config_File.get_username()
    password = Read_Config_File.get_password()
    product_name = Read_Config_File.get_product_link_text()
    first_name = Read_Config_File.get_first_name()
    last_name = Read_Config_File.get_last_name()
    pin_code = Read_Config_File.get_pin_code()
    logger = Log_Gen.log_gen()

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

