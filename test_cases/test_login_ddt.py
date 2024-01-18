import time
from selenium.webdriver.common.by import By
from Saucedemo_new_E2E_test.page_objects.login_page import LoginPage
from Saucedemo_new_E2E_test.utilities.read_properties import Read_Config_File
from Saucedemo_new_E2E_test.utilities.custom_logger import Log_Gen
from Saucedemo_new_E2E_test.utilities import excel_utils


# Test class for Data Driven Testing (DDT) on the Login page
class Test_002_DDT_Login:
    # Retrieve test data and configurations
    baseURL = Read_Config_File.get_url()
    xl_file_path = "Saucedemo_new_E2E_test/test_data/InputData.xlsx"
    # Initialize logger
    logger = Log_Gen.log_gen()

    # Test to perform Data Driven Testing for login functionality
    def test_login(self, setup):
        try:
            self.logger.info("********** Test_Login_002 **********")
            self.logger.info("********** Data Driven Testing for Login page **********")
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp = LoginPage(self.driver)
            # Get the total number of rows in the Excel sheet
            self.row_count = excel_utils.getRowCount(self.xl_file_path, 'Sheet1')
            print("No of rows presented in an XL sheet ", self.row_count)

            list_of_status = []  # Empty list variable to store test statuses

            # Loop through each row in the Excel sheet for testing
            for r in range(2, self.row_count + 1):
                # Extract data from the Excel sheet for the current row
                self.username = excel_utils.readData(self.xl_file_path, 'Sheet1', r, 1)
                self.password = excel_utils.readData(self.xl_file_path, 'Sheet1', r, 2)
                self.expected_status = excel_utils.readData(self.xl_file_path, 'Sheet1', r, 3)

                # Input login credentials and perform login
                self.lp.input_username(self.username)
                self.lp.input_password(self.password)
                self.lp.clck_login_button()
                time.sleep(2)  # Pause for stability

                # Verify the actual title after login
                actual_title_element = self.driver.find_element(By.XPATH, "//span[@class='title']")
                actual_title = actual_title_element.text
                expected_title = "Products"

                # Compare actual and expected titles, and handle test statuses
                if actual_title == expected_title:
                    if self.expected_status == "Pass":
                        self.logger.info("***** Expected 'PASS' status matches with actual status in the sheet")
                        self.lp.click_burger_menu_button()
                        self.lp.click_logout_button()
                        list_of_status.append("Pass")
                    elif self.expected_status == "Fail":
                        self.logger.info("***** Expected 'FAIL' status matches with actual status in the sheet")
                        self.lp.click_burger_menu_button()
                        self.lp.click_logout_button()
                        list_of_status.append("Fail")
                elif actual_title != expected_title:
                    if self.expected_status == "Pass":
                        self.logger.info("***** Expected status not matches with actual status in the sheet")
                        list_of_status.append("Fail")
                    elif self.expected_status == "Fail":
                        self.logger.info("***** Expected status not matches with actual status in the sheet")
                        list_of_status.append("Pass")

        except NoSuchElementException as e:
            # Handle the exception (e.g., log the error, take a screenshot, etc.)
            print(f"Element not found: {e}")

        # Finalize the test based on the collected statuses
        if "Fail" not in list_of_status:
            self.logger.info("***** Login DDT passed *****")
            assert True
        else:
            self.logger.info("***** Login DDT failed *****")
            assert False

        self.logger.info("********** Login DDT test completed **********")
        self.logger.info("********** Completed Test_002_DDT_Login **********")

