"""
Dashboard page object for OrangeHRM
"""
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.base_page import BasePage

class DashboardPage(BasePage):
    """Dashboard page object class"""
    
    # Locators
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "h6.oxd-topbar-header-breadcrumb-module")
    USER_DROPDOWN = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    PIM_MENU = (By.LINK_TEXT, "PIM")
    LEAVE_MENU = (By.LINK_TEXT, "Leave")
    ADMIN_MENU = (By.LINK_TEXT, "Admin")
    
    def __init__(self, driver):
        """Initialize dashboard page"""
        super().__init__(driver)
        self.wait_for_page_load()
    
    def wait_for_page_load(self):
        """Wait for dashboard to load"""
        self.wait_for_element(self.DASHBOARD_HEADER, timeout=15)
        self.logger.info("Dashboard page loaded successfully")
    
    def is_dashboard_loaded(self):
        """
        Verifies if dashboard is loaded
        Returns:
            bool: True if dashboard loaded
        """
        return self.is_element_visible(self.DASHBOARD_HEADER)
    
    def click_pim_menu(self):
        """Clicks on PIM menu"""
        self.click(self.PIM_MENU)
        self.sleep(2)
        self.logger.info("Clicked on PIM menu")
    
    def click_leave_menu(self):
        """Clicks on Leave menu"""
        self.click(self.LEAVE_MENU)
        self.sleep(2)
        self.logger.info("Clicked on Leave menu")
    
    def logout(self):
        """Performs logout"""
        self.logger.info("Attempting to logout")
        self.click(self.USER_DROPDOWN)
        self.sleep(1)
        self.click(self.LOGOUT_LINK)
        self.sleep(2)
        self.logger.info("Logged out successfully")
