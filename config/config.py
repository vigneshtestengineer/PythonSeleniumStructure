"""
Configuration file for OrangeHRM automation framework
"""
import os
from pathlib import Path

class Config:
    """Configuration class for framework settings"""
    
    # Project paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
    SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, 'screenshots')
    LOGS_DIR = os.path.join(REPORTS_DIR, 'logs')
    TEST_DATA_DIR = os.path.join(BASE_DIR, 'test_data')
    
    # Application URLs
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    LOGIN_URL = f"{BASE_URL}/web/index.php/auth/login"
    
    # Browser settings
    BROWSER = "chrome"  # chrome, firefox, edge
    HEADLESS = False
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30
    
    # Login credentials (OrangeHRM demo credentials)
    USERNAME = "Admin"
    PASSWORD = "admin123"
    
    # Screenshot settings
    TAKE_SCREENSHOT_ON_FAILURE = True
    
    # Logging
    LOG_LEVEL = "INFO"
    
    # Test data
    EMPLOYEE_DATA = {
        "first_name": "Test",
        "middle_name": "Auto",
        "last_name": "Employee",
        "employee_id": "",  # Will be auto-generated
    }
