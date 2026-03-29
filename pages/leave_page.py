"""
Leave page object for OrangeHRM
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.base_page import BasePage

class LeavePage(BasePage):
    """Leave page object class"""
    
    # Leave Menu Tabs
    APPLY_LEAVE_TAB = (By.LINK_TEXT, "Apply")
    MY_LEAVE_TAB = (By.LINK_TEXT, "My Leave")
    LEAVE_LIST_TAB = (By.LINK_TEXT, "Leave List")
    ASSIGN_LEAVE_TAB = (By.LINK_TEXT, "Assign Leave")
    ENTITLEMENTS_TAB = (By.LINK_TEXT, "Entitlements")
    
    # Apply Leave Form Locators
    LEAVE_TYPE_DROPDOWN = (By.CSS_SELECTOR, ".oxd-select-text-input")
    FROM_DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='yyyy-dd-mm']:first-of-type")
    TO_DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='yyyy-dd-mm']:last-of-type")
    COMMENTS_TEXTAREA = (By.CSS_SELECTOR, "textarea.oxd-textarea")
    APPLY_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    # My Leave Locators
    MY_LEAVE_RECORDS = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card")
    LEAVE_STATUS = (By.CSS_SELECTOR, ".oxd-table-cell:nth-child(6)")
    
    # Leave List Locators
    FROM_DATE_FILTER = (By.CSS_SELECTOR, "input[placeholder='From']")
    TO_DATE_FILTER = (By.CSS_SELECTOR, "input[placeholder='To']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    # Assign Leave Locators
    EMPLOYEE_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
    ASSIGN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    # Entitlements Locators
    ADD_ENTITLEMENTS_LINK = (By.LINK_TEXT, "Add Entitlements")
    EMPLOYEE_ENTITLEMENTS_LINK = (By.LINK_TEXT, "Employee Entitlements")
    MY_ENTITLEMENTS_LINK = (By.LINK_TEXT, "My Entitlements")
    
    # Common Locators
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".oxd-toast-content")
    DROPDOWN_OPTIONS = (By.CSS_SELECTOR, ".oxd-select-dropdown .oxd-select-option")
    
    def __init__(self, driver):
        """Initialize Leave page"""
        super().__init__(driver)
        self.wait_for_page_load()
    
    def wait_for_page_load(self):
        """Wait for Leave page to load"""
        self.wait_for_element(self.APPLY_LEAVE_TAB, timeout=15)
        self.logger.info("Leave page loaded successfully")
    
    # ==================== APPLY LEAVE ====================
    
    def click_apply_leave(self):
        """Clicks on Apply Leave tab"""
        self.click(self.APPLY_LEAVE_TAB)
        self.sleep(2)
        self.logger.info("Clicked on Apply Leave tab")
    
    def select_leave_type(self, leave_type="CAN - FMLA"):
        """
        Selects leave type from dropdown
        Args:
            leave_type (str): Leave type to select
        """
        self.logger.info(f"Selecting leave type: {leave_type}")
        self.click(self.LEAVE_TYPE_DROPDOWN)
        self.sleep(1)
        
        # Find and click the option
        options = self.find_elements(self.DROPDOWN_OPTIONS)
        for option in options:
            if leave_type in option.text:
                option.click()
                break
        self.sleep(1)
    
    def enter_from_date(self, date):
        """
        Enters from date
        Args:
            date (str): Date in format yyyy-mm-dd
        """
        self.logger.info(f"Entering from date: {date}")
        from_date_field = self.find_element(self.FROM_DATE_INPUT)
        from_date_field.clear()
        from_date_field.send_keys(date)
        from_date_field.send_keys(Keys.ENTER)
        self.sleep(1)
    
    def enter_to_date(self, date):
        """
        Enters to date
        Args:
            date (str): Date in format yyyy-mm-dd
        """
        self.logger.info(f"Entering to date: {date}")
        to_date_field = self.find_element(self.TO_DATE_INPUT)
        to_date_field.clear()
        to_date_field.send_keys(date)
        to_date_field.send_keys(Keys.ENTER)
        self.sleep(1)
    
    def enter_comments(self, comments):
        """
        Enters comments
        Args:
            comments (str): Leave comments
        """
        self.enter_text(self.COMMENTS_TEXTAREA, comments)
    
    def click_apply(self):
        """Clicks Apply button"""
        self.click(self.APPLY_BUTTON)
        self.sleep(2)
        self.logger.info("Clicked Apply button")
    
    def apply_leave(self, leave_type, from_date, to_date, comments=""):
        """
        Complete flow to apply leave
        Args:
            leave_type (str): Leave type
            from_date (str): From date (yyyy-mm-dd)
            to_date (str): To date (yyyy-mm-dd)
            comments (str): Comments
        """
        self.click_apply_leave()
        self.select_leave_type(leave_type)
        self.enter_from_date(from_date)
        self.enter_to_date(to_date)
        if comments:
            self.enter_comments(comments)
        self.click_apply()
    
    # ==================== MY LEAVE ====================
    
    def click_my_leave(self):
        """Clicks on My Leave tab"""
        self.click(self.MY_LEAVE_TAB)
        self.sleep(2)
        self.logger.info("Clicked on My Leave tab")
    
    def get_my_leave_records_count(self):
        """
        Gets count of leave records
        Returns:
            int: Number of leave records
        """
        records = self.find_elements(self.MY_LEAVE_RECORDS)
        count = len(records)
        self.logger.info(f"Found {count} leave records")
        return count
    
    def is_leave_record_present(self):
        """
        Checks if at least one leave record is present
        Returns:
            bool: True if record present
        """
        return self.get_my_leave_records_count() > 0
    
    # ==================== LEAVE LIST ====================
    
    def click_leave_list(self):
        """Clicks on Leave List tab"""
        self.click(self.LEAVE_LIST_TAB)
        self.sleep(2)
        self.logger.info("Clicked on Leave List tab")
    
    def search_leave_by_date_range(self, from_date, to_date):
        """
        Searches leave by date range
        Args:
            from_date (str): From date
            to_date (str): To date
        """
        self.logger.info(f"Searching leave from {from_date} to {to_date}")
        self.enter_text(self.FROM_DATE_FILTER, from_date)
        self.enter_text(self.TO_DATE_FILTER, to_date)
        self.click(self.SEARCH_BUTTON)
        self.sleep(2)
    
    # ==================== ASSIGN LEAVE ====================
    
    def click_assign_leave(self):
        """Clicks on Assign Leave tab"""
        self.click(self.ASSIGN_LEAVE_TAB)
        self.sleep(2)
        self.logger.info("Clicked on Assign Leave tab")
    
    def enter_employee_name(self, employee_name):
        """
        Enters employee name for assignment
        Args:
            employee_name (str): Employee name
        """
        self.enter_text(self.EMPLOYEE_NAME_INPUT, employee_name)
        self.sleep(1)
        # Select first autocomplete option
        first_option = (By.CSS_SELECTOR, ".oxd-autocomplete-option")
        if self.is_element_visible(first_option, timeout=3):
            self.click(first_option)
    
    def assign_leave(self, employee_name, leave_type, from_date, to_date, comments=""):
        """
        Complete flow to assign leave to employee
        Args:
            employee_name (str): Employee name
            leave_type (str): Leave type
            from_date (str): From date
            to_date (str): To date
            comments (str): Comments
        """
        self.click_assign_leave()
        self.enter_employee_name(employee_name)
        self.select_leave_type(leave_type)
        self.enter_from_date(from_date)
        self.enter_to_date(to_date)
        if comments:
            self.enter_comments(comments)
        self.click(self.ASSIGN_BUTTON)
        self.sleep(2)
    
    # ==================== ENTITLEMENTS ====================
    
    def click_entitlements(self):
        """Clicks on Entitlements tab"""
        self.click(self.ENTITLEMENTS_TAB)
        self.sleep(2)
        self.logger.info("Clicked on Entitlements tab")
    
    def click_add_entitlements(self):
        """Clicks on Add Entitlements"""
        self.click_entitlements()
        self.click(self.ADD_ENTITLEMENTS_LINK)
        self.sleep(2)
        self.logger.info("Navigated to Add Entitlements")
    
    def click_employee_entitlements(self):
        """Clicks on Employee Entitlements"""
        self.click_entitlements()
        self.click(self.EMPLOYEE_ENTITLEMENTS_LINK)
        self.sleep(2)
        self.logger.info("Navigated to Employee Entitlements")
    
    def click_my_entitlements(self):
        """Clicks on My Entitlements"""
        self.click_entitlements()
        self.click(self.MY_ENTITLEMENTS_LINK)
        self.sleep(2)
        self.logger.info("Navigated to My Entitlements")
    
    # ==================== COMMON METHODS ====================
    
    def is_success_message_displayed(self):
        """
        Checks if success message is displayed
        Returns:
            bool: True if success message displayed
        """
        return self.is_element_visible(self.SUCCESS_MESSAGE, timeout=5)
    
    def get_success_message(self):
        """
        Gets success message text
        Returns:
            str: Success message
        """
        if self.is_success_message_displayed():
            return self.get_text(self.SUCCESS_MESSAGE)
        return ""
