from selenium.webdriver.common.by import By


class LoginPage:
    # XPath's locators for web elements on the login page
    USERNAME_TEXTBOX_XPATH = "//input[@id='user-name']"
    PASSWORD_TEXTBOX_XPATH = "//input[@id='password']"
    LOGIN_BUTTON_ID = "login-button"
    BURGER_MENU_BUTTON_ID = "react-burger-menu-btn"
    LOGOUT_BUTTON_ID = "logout_sidebar_link"  # Assuming the correct ID for the logout button

    def __init__(self, driver):
        """
        Constructor for the LoginPage class.

        :param driver: The WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def enter_username(self, username):
        """
        Enters the username in the corresponding input field on the login page.

        :param username: The username to be entered.
        """
        username_element = self.driver.find_element(By.XPATH, self.USERNAME_TEXTBOX_XPATH)
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password):
        """
        Enters the password in the corresponding input field on the login page.

        :param password: The password to be entered.
        """
        password_element = self.driver.find_element(By.XPATH, self.PASSWORD_TEXTBOX_XPATH)
        password_element.clear()
        password_element.send_keys(password)

    def click_login_button(self):
        """
        Clicks the 'Login' button on the login page.
        """
        self.driver.find_element(By.ID, self.LOGIN_BUTTON_ID).click()

    def click_burger_menu_button(self):
        """
        Clicks the burger menu button on the login page.
        """
        self.driver.find_element(By.ID, self.BURGER_MENU_BUTTON_ID).click()

    def click_logout_button(self):
        """
        Clicks the logout button on the login page.
        """
        self.driver.find_element(By.ID, self.LOGOUT_BUTTON_ID).click()
