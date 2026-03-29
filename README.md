# OrangeHRM Selenium Automation Framework

## 📋 Project Overview
Comprehensive Selenium WebDriver automation framework for OrangeHRM using Python, Pytest, and Page Object Model (POM) design pattern.

## 🎯 Test Coverage
This framework automates the complete OrangeHRM workflow:

### ✅ Covered Functionality:
1. **Login**
   - Successful login with valid credentials
   - Dashboard verification

2. **PIM (Personnel Information Management)**
   - Add Employee
   - Search Employee (by ID and Name)
   - Edit Employee Details
   - Delete Employee Record
   - Configuration → Data Import

3. **Leave Management**
   - Apply Leave
   - View Leave List
   - Check My Leave
   - Assign Leave
   - Manage Entitlements (Add, Employee, My Entitlements)

4. **Logout**
   - User logout verification

## 🏗️ Framework Structure

```
orangehrm_automation/
│
├── config/
│   ├── __init__.py
│   └── config.py                  # Configuration settings
│
├── pages/                         # Page Object Model
│   ├── __init__.py
│   ├── base_page.py              # Base page with common methods
│   ├── login_page.py             # Login page object
│   ├── dashboard_page.py         # Dashboard page object
│   ├── pim_page.py               # PIM module page object
│   └── leave_page.py             # Leave module page object
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py               # Pytest fixtures and hooks
│   └── test_orangehrm_workflow.py # Main test suite
│
├── utilities/
│   ├── __init__.py
│   ├── driver_factory.py         # WebDriver factory
│   ├── logger.py                 # Custom logging utility
│   └── screenshot.py             # Screenshot utility
│
├── test_data/                    # Test data files
│
├── reports/
│   ├── screenshots/              # Failure screenshots
│   └── logs/                     # Test execution logs
│
├── requirements.txt              # Python dependencies
├── pytest.ini                    # Pytest configuration
└── README.md                     # This file
```

## 🚀 Installation & Setup

### Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)
- Google Chrome or Firefox browser

### Step 1: Clone/Download the Project
```bash
# If you have the zip file, extract it
# Or clone from repository
cd orangehrm_automation
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- selenium (WebDriver)
- pytest (Test framework)
- pytest-html (HTML reports)
- webdriver-manager (Auto driver management)
- openpyxl (Excel support)
- Faker (Test data generation)

## 🎮 Running Tests

### Run All Tests (Complete E2E Workflow):
```bash
pytest tests/test_orangehrm_workflow.py
```

### Run Specific Test Class:
```bash
# Run complete workflow
pytest tests/test_orangehrm_workflow.py::TestOrangeHRMWorkflow

# Run smoke test only
pytest tests/test_orangehrm_workflow.py::TestLoginOnly
```

### Run Specific Test Method:
```bash
pytest tests/test_orangehrm_workflow.py::TestOrangeHRMWorkflow::test_01_login
```

### Run Tests by Markers:
```bash
# Run smoke tests
pytest -m smoke

# Run e2e tests
pytest -m e2e

# Run regression suite
pytest -m regression
```

### Run with Different Options:
```bash
# Verbose output
pytest -v

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run in headless mode (modify config.py: HEADLESS = True)
pytest

# Generate HTML report
pytest --html=reports/custom_report.html
```

## 📊 Test Reports

### HTML Report:
After test execution, open:
```
reports/report.html
```

### Log Files:
Check detailed logs in:
```
reports/logs/test_log_YYYYMMDD_HHMMSS.log
reports/logs/pytest.log
```

### Screenshots:
Failed test screenshots are saved in:
```
reports/screenshots/
```

## ⚙️ Configuration

Edit `config/config.py` to modify:

```python
# Browser settings
BROWSER = "chrome"  # or "firefox"
HEADLESS = False    # Set True for headless execution

# Timeouts
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20
PAGE_LOAD_TIMEOUT = 30

# Test data
EMPLOYEE_DATA = {
    "first_name": "Test",
    "middle_name": "Auto",
    "last_name": "Employee"
}
```

## 🎯 Test Execution Flow

The complete workflow executes in this order:

1. ✅ **test_01_login** - Login verification
2. ✅ **test_02_navigate_to_pim** - PIM module navigation
3. ✅ **test_03_add_employee** - Add new employee
4. ✅ **test_04_search_employee_by_id** - Search by employee ID
5. ✅ **test_05_search_employee_by_name** - Search by name
6. ✅ **test_06_edit_employee_details** - Edit employee info
7. ✅ **test_07_configuration_data_import** - Data import page
8. ✅ **test_08_navigate_to_leave** - Leave module navigation
9. ✅ **test_09_apply_leave** - Apply for leave
10. ✅ **test_10_view_leave_list** - View leave list
11. ✅ **test_11_check_my_leave** - Check my leave
12. ✅ **test_12_assign_leave** - Assign leave page
13. ✅ **test_13_manage_entitlements** - Entitlements management
14. ✅ **test_14_delete_employee** - Delete employee record
15. ✅ **test_15_logout** - Logout verification

## 📝 Test Assertions

Each test includes meaningful assertions:
- ✅ Login success verification
- ✅ Page load confirmations
- ✅ Element visibility checks
- ✅ Success message validations
- ✅ Data validation (add/search/edit/delete)
- ✅ URL verification
- ✅ Logout confirmation

## 🎨 Locator Strategy

Following best practices with descriptive locators:
- ✅ **Prefer**: CSS Selectors, IDs, Link Text
- ✅ **Use**: Relative XPaths when necessary
- ❌ **Avoid**: Brittle absolute XPaths

Example:
```python
# Good locators
USERNAME_INPUT = (By.NAME, "username")
LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
PIM_MENU = (By.LINK_TEXT, "PIM")

# Relative XPath when needed
EMPLOYEE_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
```

## 🐛 Troubleshooting

### Common Issues:

**1. WebDriver not found:**
```bash
# The framework uses webdriver-manager, it auto-downloads drivers
# Just ensure you have internet connection on first run
```

**2. Element not found:**
```bash
# Increase wait times in config.py
EXPLICIT_WAIT = 30
```

**3. Tests failing randomly:**
```bash
# Check your internet connection
# OrangeHRM demo site might be slow
# Increase implicit/explicit waits
```

**4. Import errors:**
```bash
# Ensure you're in the project root directory
cd orangehrm_automation
pytest tests/
```

## 📈 Extending the Framework

### Add New Page Object:
1. Create file in `pages/` directory
2. Inherit from `BasePage`
3. Define locators and methods
4. Import in test files

### Add New Test:
1. Create test file in `tests/` directory
2. Follow naming: `test_*.py`
3. Import page objects
4. Write test methods starting with `test_`

### Add Test Data:
1. Create JSON/Excel file in `test_data/`
2. Use utilities to read data
3. Parameterize tests with data

## 🏆 Best Practices Implemented

- ✅ **Page Object Model (POM)** - Separation of concerns
- ✅ **DRY Principle** - Reusable methods in BasePage
- ✅ **Descriptive Naming** - Clear test and method names
- ✅ **Logging** - Comprehensive logging at each step
- ✅ **Screenshots** - Auto-capture on failure
- ✅ **Assertions** - Meaningful validations
- ✅ **Independent Tests** - Each test can run standalone
- ✅ **Configuration Management** - Centralized config
- ✅ **Wait Strategies** - Explicit and implicit waits

## 📞 Support

For issues or questions:
1. Check logs in `reports/logs/`
2. Review screenshots in `reports/screenshots/`
3. Verify configuration in `config/config.py`

## 📄 License

This framework is created for educational and testing purposes.

## 👨‍💻 Author

**Vignesh K.V.**
- Specialist Engineer QA
- Email: vignesh1611589@gmail.com
- LinkedIn: [linkedin.com/in/vignesh-kv-941b52186](https://www.linkedin.com/in/vignesh-kv-941b52186)

---

**Happy Testing! 🚀**
