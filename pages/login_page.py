"""
Login page object for OrangeHRM
"""
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    """Login page object class"""
    
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content")
    LOGO = (By.CSS_SELECTOR, ".orangehrm-login-branding img")
    
    def __init__(self, driver):
        """Initialize login page"""
        super().__init__(driver)
        self.driver.get(Config.LOGIN_URL)
        self.wait_for_page_load()
    
    def wait_for_page_load(self):
        """Wait for login page to load"""
        self.wait_for_element(self.USERNAME_INPUT)
        self.logger.info("Login page loaded successfully")
    
    def enter_username(self, username):
        """
        Enters username
        Args:
            username (str): Username to enter
        """
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """
        Enters password
        Args:
            password (str): Password to enter
        """
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Clicks login button"""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Performs complete login action
        Args:
            username (str): Username
            password (str): Password
        """
        self.logger.info(f"Attempting login with username: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.sleep(2)  # Wait for login to complete
    
    def get_error_message(self):
        """
        Gets error message text
        Returns:
            str: Error message
        """
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """
        Checks if error message is displayed
        Returns:
            bool: True if error displayed
        """
        return self.is_element_visible(self.ERROR_MESSAGE)
