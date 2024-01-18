import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup():
    ChromeDriverManager().install()
    driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    driver.maximize_window()
    return driver
    # yield driver
    # driver.quit()


# @pytest.fixture()
# def setup(browser):
#     if browser == "chromium":
#         ChromeDriverManager().install()
#         driver = webdriver.Chrome(options=webdriver.ChromeOptions())
#         driver.maximize_window()
#         print("launched chrome browser")
#     elif browser == "firefox":
#         GeckoDriverManager().install()
#         driver = webdriver.Firefox(options=webdriver.FirefoxOptions())
#         driver.maximize_window()
#         print("launched firefox browser")
#     else:
#         print("user should pass any one browser")
#
#     return driver
#
#
# def pytest_adoption(parser):      # this will get the value from CLI
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):             # this will return the browser value to the setup method
#     return request.config.getoption("--browser")


# --------------------------------------------------------------------------------------------

# # it is hook for adding environment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = "Sauce demo E2E testing"
#     config._metadata['Module Name'] = "E-Commerce"
#     config._metadata['Tester'] = 'Leo12345'
#
# # it is hook to delete/modify Environmental info to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

