"""
PIM (Personnel Information Management) page object for OrangeHRM
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.base_page import BasePage

class PIMPage(BasePage):
    """PIM page object class"""
    
    # Main PIM Locators
    ADD_EMPLOYEE_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--secondary:not(.oxd-button--label-danger)")
    EMPLOYEE_LIST_TAB = (By.LINK_TEXT, "Employee List")
    CONFIGURATION_MENU = (By.CSS_SELECTOR, "span.oxd-topbar-body-nav-tab-item")
    
    # Add Employee Form Locators
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    MIDDLE_NAME_INPUT = (By.NAME, "middleName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMPLOYEE_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".oxd-toast-content")
    
    # Search Employee Locators
    EMPLOYEE_NAME_SEARCH = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
    EMPLOYEE_ID_SEARCH = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RESET_BUTTON = (By.CSS_SELECTOR, "button[type='button'].oxd-button--ghost")
    
    # Employee Records Table
    EMPLOYEE_RECORDS_TABLE = (By.CSS_SELECTOR, ".oxd-table-body")
    EMPLOYEE_ROW = (By.CSS_SELECTOR, ".oxd-table-card")
    EMPLOYEE_NAME_CELL = (By.CSS_SELECTOR, ".oxd-table-cell:nth-child(3)")
    EMPLOYEE_ID_CELL = (By.CSS_SELECTOR, ".oxd-table-cell:nth-child(2)")
    EDIT_BUTTON = (By.CSS_SELECTOR, "i.bi-pencil-fill")
    DELETE_BUTTON = (By.CSS_SELECTOR, "i.bi-trash")
    DELETE_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button.oxd-button--label-danger")
    
    # Edit Employee Locators
    PERSONAL_DETAILS_TAB = (By.LINK_TEXT, "Personal Details")
    CONTACT_DETAILS_TAB = (By.LINK_TEXT, "Contact Details")
    
    # Configuration Locators
    DATA_IMPORT_LINK = (By.LINK_TEXT, "Data Import")
    IMPORT_FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    
    def __init__(self, driver):
        """Initialize PIM page"""
        super().__init__(driver)
        self.wait_for_page_load()
    
    def wait_for_page_load(self):
        """Wait for PIM page to load"""
        self.wait_for_element(self.ADD_EMPLOYEE_BUTTON, timeout=15)
        self.logger.info("PIM page loaded successfully")
    
    # ==================== ADD EMPLOYEE ====================
    
    def click_add_employee(self):
        """Clicks on Add Employee button"""
        self.click(self.ADD_EMPLOYEE_BUTTON)
        self.sleep(1)
        self.logger.info("Clicked on Add Employee button")
    
    def fill_employee_details(self, first_name, middle_name="", last_name="", employee_id=None):
        """
        Fills employee details form
        Args:
            first_name (str): First name
            middle_name (str): Middle name
            last_name (str): Last name
            employee_id (str): Employee ID (optional)
        Returns:
            str: Generated/provided employee ID
        """
        self.logger.info(f"Filling employee details: {first_name} {middle_name} {last_name}")
        
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        if middle_name:
            self.enter_text(self.MIDDLE_NAME_INPUT, middle_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        
        # Get the auto-generated employee ID if not provided
        if employee_id:
            emp_id_field = self.find_element(self.EMPLOYEE_ID_INPUT)
            emp_id_field.clear()
            emp_id_field.send_keys(employee_id)
            generated_id = employee_id
        else:
            emp_id_field = self.find_element(self.EMPLOYEE_ID_INPUT)
            generated_id = emp_id_field.get_attribute('value')
        
        self.logger.info(f"Employee ID: {generated_id}")
        return generated_id
    
    def click_save(self):
        """Clicks save button"""
        self.click(self.SAVE_BUTTON)
        self.sleep(2)
        self.logger.info("Clicked Save button")
    
    def add_employee(self, first_name, middle_name="", last_name=""):
        """
        Complete flow to add an employee
        Args:
            first_name (str): First name
            middle_name (str): Middle name
            last_name (str): Last name
        Returns:
            str: Employee ID
        """
        self.click_add_employee()
        employee_id = self.fill_employee_details(first_name, middle_name, last_name)
        self.click_save()
        return employee_id
    
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
    
    # ==================== SEARCH EMPLOYEE ====================
    
    def navigate_to_employee_list(self):
        """Navigates to employee list"""
        self.click(self.EMPLOYEE_LIST_TAB)
        self.sleep(2)
        self.logger.info("Navigated to Employee List")
    
    def search_employee_by_id(self, employee_id):
        """
        Searches employee by ID
        Args:
            employee_id (str): Employee ID to search
        """
        self.logger.info(f"Searching employee with ID: {employee_id}")
        self.enter_text(self.EMPLOYEE_ID_SEARCH, employee_id)
        self.click(self.SEARCH_BUTTON)
        self.sleep(2)
    
    def search_employee_by_name(self, employee_name):
        """
        Searches employee by name
        Args:
            employee_name (str): Employee name to search
        """
        self.logger.info(f"Searching employee with name: {employee_name}")
        self.enter_text(self.EMPLOYEE_NAME_SEARCH, employee_name)
        self.sleep(1)  # Wait for autocomplete
        # Select first option from dropdown
        first_option = (By.CSS_SELECTOR, ".oxd-autocomplete-option")
        if self.is_element_visible(first_option, timeout=3):
            self.click(first_option)
        self.click(self.SEARCH_BUTTON)
        self.sleep(2)
    
    def get_search_results_count(self):
        """
        Gets count of search results
        Returns:
            int: Number of records found
        """
        records = self.find_elements(self.EMPLOYEE_ROW)
        count = len(records)
        self.logger.info(f"Found {count} employee records")
        return count
    
    def is_employee_found(self):
        """
        Checks if employee is found in search results
        Returns:
            bool: True if employee found
        """
        return self.get_search_results_count() > 0
    
    # ==================== EDIT EMPLOYEE ====================
    
    def click_edit_first_employee(self):
        """Clicks edit button for first employee in list"""
        edit_buttons = self.find_elements(self.EDIT_BUTTON)
        if edit_buttons:
            edit_buttons[0].click()
            self.sleep(2)
            self.logger.info("Clicked Edit button for first employee")
        else:
            self.logger.error("No edit button found")
    
    def edit_employee_first_name(self, new_first_name):
        """
        Edits employee first name
        Args:
            new_first_name (str): New first name
        """
        self.logger.info(f"Editing employee first name to: {new_first_name}")
        first_name_field = self.find_element(self.FIRST_NAME_INPUT)
        first_name_field.clear()
        first_name_field.send_keys(new_first_name)
        self.click_save()
    
    # ==================== DELETE EMPLOYEE ====================
    
    def click_delete_first_employee(self):
        """Clicks delete button for first employee in list"""
        delete_buttons = self.find_elements(self.DELETE_BUTTON)
        if delete_buttons:
            delete_buttons[0].click()
            self.sleep(1)
            self.logger.info("Clicked Delete button for first employee")
        else:
            self.logger.error("No delete button found")
    
    def confirm_delete(self):
        """Confirms deletion in popup"""
        self.click(self.DELETE_CONFIRM_BUTTON)
        self.sleep(2)
        self.logger.info("Confirmed employee deletion")
    
    def delete_employee(self):
        """
        Complete flow to delete an employee
        """
        self.click_delete_first_employee()
        self.confirm_delete()
    
    # ==================== CONFIGURATION - DATA IMPORT ====================
    
    def navigate_to_configuration(self):
        """Navigates to Configuration menu"""
        configuration_tabs = self.find_elements(self.CONFIGURATION_MENU)
        if len(configuration_tabs) > 1:
            configuration_tabs[1].click()  # Second tab is usually Configuration
            self.sleep(1)
            self.logger.info("Clicked on Configuration menu")
    
    def click_data_import(self):
        """Clicks on Data Import link"""
        self.navigate_to_configuration()
        self.sleep(1)
        self.click(self.DATA_IMPORT_LINK)
        self.sleep(2)
        self.logger.info("Navigated to Data Import")
    
    def is_data_import_page_loaded(self):
        """
        Checks if Data Import page is loaded
        Returns:
            bool: True if loaded
        """
        return self.is_element_visible(self.IMPORT_FILE_INPUT, timeout=5)
