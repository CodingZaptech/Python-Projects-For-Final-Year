# CheckTheURLBackend.py
# Backend logic for checking URL with Selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

class URLChecker:
    def __init__(self):
        # Chrome options for headless browsing
        self.options = Options()
        self.options.headless = True

    def check_url(self, url: str):
        """Open URL and verify if page loads correctly."""
        try:
            service = Service()  # path to chromedriver if needed
            driver = webdriver.Chrome(service=service, options=self.options)
            driver.get(url)
            print(f"Website title: {driver.title}")
            driver.quit()
        except WebDriverException as e:
            print(f"Error: {e}")
