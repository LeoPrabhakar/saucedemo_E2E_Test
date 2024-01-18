import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from ..page_objects.login_page import LoginPage
from Saucedemo_new_E2E_test.page_objects.login_page import LoginPage
from Saucedemo_new_E2E_test.utilities.read_properties import Read_Config_File
from Saucedemo_new_E2E_test.utilities.custom_logger import Log_Gen

# Define a test class for login functionality
class Test_001_Login:
    # Retrieve test data and configurations
    baseURL = Read_Config_File.get_url()
    username = Read_Config_File.get_username()
    password = Read_Config_File.get_password()
    # Initialize logger
    logger = Log_Gen.log_gen()

    # Test to verify the home page title
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

    # Test to perform login and verify the Products page title
    def test_login(self, setup):
        self.logger.info("********** Test_Login_001 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        # Input login credentials
        self.lp.input_username(self.username)
        self.lp.input_password(self.password)
        self.lp.clck_login_button()
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
        self.lp.click_logout_button()
