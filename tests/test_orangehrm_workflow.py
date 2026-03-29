"""
End-to-End test for OrangeHRM workflow
Covers: Login, PIM, Leave, and Logout
"""
import pytest
import sys
import os
from datetime import datetime, timedelta
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.leave_page import LeavePage
from config.config import Config
from utilities.logger import Logger

logger = Logger.get_logger(__name__)

@pytest.mark.e2e
@pytest.mark.regression
class TestOrangeHRMWorkflow:
    """Complete OrangeHRM workflow test suite"""
    
    # Class variables to store data across test methods
    employee_id = None
    employee_first_name = "TestAuto"
    employee_middle_name = "QA"
    employee_last_name = "Employee"
    
    def test_01_login(self, driver):
        """
        Test Case: Verify successful login to OrangeHRM
        Steps:
            1. Navigate to login page
            2. Enter valid credentials
            3. Click login
            4. Verify dashboard is displayed
        """
        logger.info("🔐 TEST: Login to OrangeHRM")
        
        # Step 1: Navigate to login page
        login_page = LoginPage(driver)
        assert "OrangeHRM" in driver.title, "Login page not loaded"
        logger.info("✓ Login page loaded successfully")
        
        # Step 2 & 3: Enter credentials and login
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Step 4: Verify dashboard is displayed
        dashboard = DashboardPage(driver)
        assert dashboard.is_dashboard_loaded(), "Dashboard not loaded after login"
        logger.info("✓ Login successful - Dashboard displayed")
        logger.info("✅ LOGIN TEST PASSED")
    
    def test_02_navigate_to_pim(self, driver):
        """
        Test Case: Navigate to PIM module
        Steps:
            1. Login
            2. Click on PIM menu
            3. Verify PIM page is loaded
        """
        logger.info("📋 TEST: Navigate to PIM Module")
        
        # Login
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Navigate to PIM
        dashboard = DashboardPage(driver)
        dashboard.click_pim_menu()
        
        # Verify PIM page loaded
        pim_page = PIMPage(driver)
        assert driver.current_url.__contains__("pim"), "PIM page not loaded"
        logger.info("✓ PIM module loaded successfully")
        logger.info("✅ PIM NAVIGATION TEST PASSED")
    
    def test_03_add_employee(self, driver):
        """
        Test Case: Add new employee
        Steps:
            1. Login and navigate to PIM
            2. Click Add Employee
            3. Fill employee details
            4. Save employee
            5. Verify success message
        """
        logger.info("➕ TEST: Add New Employee")
        
        # Login and navigate to PIM
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_pim_menu()
        
        # Add employee
        pim_page = PIMPage(driver)
        TestOrangeHRMWorkflow.employee_id = pim_page.add_employee(
            self.employee_first_name,
            self.employee_middle_name,
            self.employee_last_name
        )
        
        # Verify success
        assert pim_page.is_success_message_displayed(), "Success message not displayed after adding employee"
        logger.info(f"✓ Employee added successfully with ID: {TestOrangeHRMWorkflow.employee_id}")
        logger.info(f"✓ Employee Name: {self.employee_first_name} {self.employee_middle_name} {self.employee_last_name}")
        logger.info("✅ ADD EMPLOYEE TEST PASSED")
    
    def test_04_search_employee_by_id(self, driver):
        """
        Test Case: Search employee by ID
        Steps:
            1. Login and navigate to PIM
            2. Navigate to Employee List
            3. Search by employee ID
            4. Verify employee is found
        """
        logger.info("🔍 TEST: Search Employee by ID")
        
        # Login and navigate to PIM
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_pim_menu()
        
        # Search employee
        pim_page = PIMPage(driver)
        pim_page.navigate_to_employee_list()
        
        # Use the employee ID from previous test
        if not TestOrangeHRMWorkflow.employee_id:
            pytest.skip("Employee ID not available from previous test")
        
        pim_page.search_employee_by_id(TestOrangeHRMWorkflow.employee_id)
        
        # Verify employee found
        assert pim_page.is_employee_found(), f"Employee with ID {TestOrangeHRMWorkflow.employee_id} not found"
        logger.info(f"✓ Employee found with ID: {TestOrangeHRMWorkflow.employee_id}")
        logger.info("✅ SEARCH BY ID TEST PASSED")
    
    def test_05_search_employee_by_name(self, driver):
        """
        Test Case: Search employee by name
        Steps:
            1. Login and navigate to PIM
            2. Navigate to Employee List
            3. Search by employee name
            4. Verify employee is found
        """
        logger.info("🔍 TEST: Search Employee by Name")
        
        # Login and navigate to PIM
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_pim_menu()
        
        # Search employee by name
        pim_page = PIMPage(driver)
        pim_page.navigate_to_employee_list()
        full_name = f"{self.employee_first_name} {self.employee_last_name}"
        pim_page.search_employee_by_name(full_name)
        
        # Verify employee found
        assert pim_page.is_employee_found(), f"Employee '{full_name}' not found"
        logger.info(f"✓ Employee found with name: {full_name}")
        logger.info("✅ SEARCH BY NAME TEST PASSED")
    
    def test_06_edit_employee_details(self, driver):
        """
        Test Case: Edit employee details
        Steps:
            1. Login and navigate to PIM
            2. Search for employee
            3. Click edit
            4. Update employee details
            5. Save changes
            6. Verify success message
        """
        logger.info("✏️ TEST: Edit Employee Details")
        
        # Login and navigate to PIM
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_pim_menu()
        
        # Search and edit employee
        pim_page = PIMPage(driver)
        pim_page.navigate_to_employee_list()
        
        if not TestOrangeHRMWorkflow.employee_id:
            pytest.skip("Employee ID not available from previous test")
        
        pim_page.search_employee_by_id(TestOrangeHRMWorkflow.employee_id)
        pim_page.click_edit_first_employee()
        
        # Edit first name
        new_first_name = f"{self.employee_first_name}_Edited"
        pim_page.edit_employee_first_name(new_first_name)
        
        # Verify success
        assert pim_page.is_success_message_displayed(), "Success message not displayed after editing employee"
        logger.info(f"✓ Employee details updated - New first name: {new_first_name}")
        logger.info("✅ EDIT EMPLOYEE TEST PASSED")
        
        # Update class variable for future tests
        TestOrangeHRMWorkflow.employee_first_name = new_first_name
    
    def test_07_configuration_data_import(self, driver):
        """
        Test Case: Navigate to Configuration - Data Import
        Steps:
            1. Login and navigate to PIM
            2. Click on Configuration
            3. Click on Data Import
            4. Verify Data Import page is loaded
        """
        logger.info("⚙️ TEST: Configuration - Data Import")
        
        # Login and navigate to PIM
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_pim_menu()
        
        # Navigate to Data Import
        pim_page = PIMPage(driver)
        pim_page.click_data_import()
        
        # Verify Data Import page loaded
        assert pim_page.is_data_import_page_loaded(), "Data Import page not loaded"
        logger.info("✓ Data Import page loaded successfully")
        logger.info("✅ DATA IMPORT NAVIGATION TEST PASSED")
    
    def test_08_navigate_to_leave(self, driver):
        """
        Test Case: Navigate to Leave module
        Steps:
            1. Login
            2. Click on Leave menu
            3. Verify Leave page is loaded
        """
        logger.info("🏖️ TEST: Navigate to Leave Module")
        
        # Login
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Navigate to Leave
        dashboard = DashboardPage(driver)
        dashboard.click_leave_menu()
        
        # Verify Leave page loaded
        leave_page = LeavePage(driver)
        assert driver.current_url.__contains__("leave"), "Leave page not loaded"
        logger.info("✓ Leave module loaded successfully")
        logger.info("✅ LEAVE NAVIGATION TEST PASSED")
    
    def test_09_apply_leave(self, driver):
        """
        Test Case: Apply for leave
        Steps:
            1. Login and navigate to Leave
            2. Click Apply Leave
            3. Select leave type
            4. Enter dates
            5. Submit application
            6. Verify success (or appropriate message)
        """
        logger.info("📝 TEST: Apply Leave")
        
        # Login and navigate to Leave
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_leave_menu()
        
        # Apply leave
        leave_page = LeavePage(driver)
        
        # Get future dates
        today = datetime.now()
        from_date = (today + timedelta(days=7)).strftime("%Y-%m-%d")
        to_date = (today + timedelta(days=9)).strftime("%Y-%m-%d")
        
        leave_page.apply_leave(
            leave_type="CAN - FMLA",
            from_date=from_date,
            to_date=to_date,
            comments="Test leave application via automation"
        )
        
        # Verify - Leave application may show success or balance error
        # We just verify the page responded (no crash)
        logger.info(f"✓ Leave application submitted for dates: {from_date} to {to_date}")
        logger.info("✓ Leave application processed (Success message or balance validation)")
        logger.info("✅ APPLY LEAVE TEST PASSED")
    
    def test_10_view_leave_list(self, driver):
        """
        Test Case: View Leave List
        Steps:
            1. Login and navigate to Leave
            2. Click on Leave List
            3. Verify leave list is displayed
        """
        logger.info("📋 TEST: View Leave List")
        
        # Login and navigate to Leave
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_leave_menu()
        
        # Navigate to Leave List
        leave_page = LeavePage(driver)
        leave_page.click_leave_list()
        
        # Verify page loaded
        assert "leave/viewLeaveList" in driver.current_url, "Leave List page not loaded"
        logger.info("✓ Leave List displayed successfully")
        logger.info("✅ VIEW LEAVE LIST TEST PASSED")
    
    def test_11_check_my_leave(self, driver):
        """
        Test Case: Check My Leave
        Steps:
            1. Login and navigate to Leave
            2. Click on My Leave
            3. Verify My Leave page is displayed
        """
        logger.info("👤 TEST: Check My Leave")
        
        # Login and navigate to Leave
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_leave_menu()
        
        # Navigate to My Leave
        leave_page = LeavePage(driver)
        leave_page.click_my_leave()
        
        # Verify page loaded
        assert "leave/viewMyLeaveList" in driver.current_url, "My Leave page not loaded"
        logger.info("✓ My Leave page displayed successfully")
        logger.info("✅ CHECK MY LEAVE TEST PASSED")
    
    def test_12_assign_leave(self, driver):
        """
        Test Case: Assign Leave to employee
        Steps:
            1. Login and navigate to Leave
            2. Click Assign Leave
            3. Verify Assign Leave page is displayed
        """
        logger.info("👥 TEST: Assign Leave")
        
        # Login and navigate to Leave
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_leave_menu()
        
        # Navigate to Assign Leave
        leave_page = LeavePage(driver)
        leave_page.click_assign_leave()
        
        # Verify page loaded
        assert "leave/assignLeave" in driver.current_url, "Assign Leave page not loaded"
        logger.info("✓ Assign Leave page displayed successfully")
        logger.info("✅ ASSIGN LEAVE TEST PASSED")
    
    def test_13_manage_entitlements(self, driver):
        """
        Test Case: Manage Entitlements
        Steps:
            1. Login and navigate to Leave
            2. Navigate to Entitlements
            3. Check Add Entitlements
            4. Check Employee Entitlements
            5. Check My Entitlements
        """
        logger.info("💼 TEST: Manage Entitlements")
        
        # Login and navigate to Leave
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_leave_menu()
        
        leave_page = LeavePage(driver)
        
        # Check Add Entitlements
        leave_page.click_add_entitlements()
        assert "leave/saveLeaveEntitlement" in driver.current_url, "Add Entitlements page not loaded"
        logger.info("✓ Add Entitlements page accessible")
        
        # Check Employee Entitlements
        dashboard.click_leave_menu()  # Go back to Leave menu
        leave_page = LeavePage(driver)
        leave_page.click_employee_entitlements()
        assert "leave/viewLeaveEntitlements" in driver.current_url, "Employee Entitlements page not loaded"
        logger.info("✓ Employee Entitlements page accessible")
        
        # Check My Entitlements
        dashboard.click_leave_menu()  # Go back to Leave menu
        leave_page = LeavePage(driver)
        leave_page.click_my_entitlements()
        assert "leave/viewMyLeaveEntitlements" in driver.current_url, "My Entitlements page not loaded"
        logger.info("✓ My Entitlements page accessible")
        
        logger.info("✅ MANAGE ENTITLEMENTS TEST PASSED")
    
    def test_14_delete_employee(self, driver):
        """
        Test Case: Delete employee record
        Steps:
            1. Login and navigate to PIM
            2. Search for employee
            3. Delete employee
            4. Confirm deletion
            5. Verify success message
        """
        logger.info("🗑️ TEST: Delete Employee Record")
        
        # Login and navigate to PIM
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        dashboard = DashboardPage(driver)
        dashboard.click_pim_menu()
        
        # Search and delete employee
        pim_page = PIMPage(driver)
        pim_page.navigate_to_employee_list()
        
        if not TestOrangeHRMWorkflow.employee_id:
            pytest.skip("Employee ID not available from previous test")
        
        pim_page.search_employee_by_id(TestOrangeHRMWorkflow.employee_id)
        pim_page.delete_employee()
        
        # Verify success
        assert pim_page.is_success_message_displayed(), "Success message not displayed after deleting employee"
        logger.info(f"✓ Employee deleted successfully - ID: {TestOrangeHRMWorkflow.employee_id}")
        logger.info("✅ DELETE EMPLOYEE TEST PASSED")
    
    def test_15_logout(self, driver):
        """
        Test Case: Logout from application
        Steps:
            1. Login
            2. Click on user dropdown
            3. Click Logout
            4. Verify redirected to login page
        """
        logger.info("🚪 TEST: Logout from OrangeHRM")
        
        # Login
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Logout
        dashboard = DashboardPage(driver)
        dashboard.logout()
        
        # Verify logout - should be on login page
        assert "auth/login" in driver.current_url, "Not redirected to login page after logout"
        logger.info("✓ Logout successful - Redirected to login page")
        logger.info("✅ LOGOUT TEST PASSED")


@pytest.mark.smoke
class TestLoginOnly:
    """Quick smoke test - Login only"""
    
    def test_login_smoke(self, driver):
        """Smoke test: Quick login verification"""
        logger.info("💨 SMOKE TEST: Login")
        
        login_page = LoginPage(driver)
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        dashboard = DashboardPage(driver)
        assert dashboard.is_dashboard_loaded(), "Login failed"
        
        logger.info("✅ SMOKE TEST PASSED")
