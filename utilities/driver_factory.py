"""
WebDriver factory for creating browser instances
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import Config

class DriverFactory:
    """Factory class to create WebDriver instances"""
    
    @staticmethod
    def get_driver(browser=None):
        """
        Creates and returns WebDriver instance
        Args:
            browser (str): Browser name (chrome, firefox)
        Returns:
            WebDriver: Selenium WebDriver instance
        """
        browser = browser or Config.BROWSER
        
        if browser.lower() == "chrome":
            chrome_options = ChromeOptions()
            if Config.HEADLESS:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
        elif browser.lower() == "firefox":
            firefox_options = FirefoxOptions()
            if Config.HEADLESS:
                firefox_options.add_argument("--headless")
            
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        
        return driver
