from pages.home_page import FirstPage
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Base class of each test
    """
    def setUp(self):
    # 1. Open Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    # Get runcolors
        self.driver.get("https://runcolors.com")
    #Create HomePage instance
        self.home_page_object = FirstPage(self.driver)

    # 2. Accept cookies
        self.home_page_object.accept_cookies()


    def tearDown(self):
        self.driver.quit()
