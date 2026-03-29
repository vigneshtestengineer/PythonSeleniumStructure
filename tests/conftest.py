"""
Pytest fixtures and hooks for OrangeHRM automation
"""
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utilities.driver_factory import DriverFactory
from utilities.screenshot import Screenshot
from utilities.logger import Logger

logger = Logger.get_logger(__name__)

@pytest.fixture(scope="function")
def driver(request):
    """
    WebDriver fixture - creates and quits driver for each test
    """
    logger.info("=" * 80)
    logger.info("Initializing WebDriver")
    driver = DriverFactory.get_driver()
    yield driver
    logger.info("Quitting WebDriver")
    driver.quit()
    logger.info("=" * 80)

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    """
    Session-level setup and teardown
    """
    logger.info("=" * 80)
    logger.info("TEST SESSION STARTED - OrangeHRM Automation")
    logger.info("=" * 80)
    yield
    logger.info("=" * 80)
    logger.info("TEST SESSION COMPLETED")
    logger.info("=" * 80)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and take screenshots on failure
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        if report.failed:
            driver = item.funcargs.get('driver')
            if driver:
                test_name = item.name
                screenshot_path = Screenshot.take_screenshot(driver, test_name)
                logger.error(f"❌ Test failed: {test_name}")
                logger.info(f"📸 Screenshot saved: {screenshot_path}")
        elif report.passed:
            logger.info(f"✅ Test passed: {item.name}")

def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "smoke: Smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: Regression tests"
    )
    config.addinivalue_line(
        "markers", "e2e: End-to-end tests"
    )
