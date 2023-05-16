from pages.base_page import BasePage
from Locators.Locators import Locators

class FirstPage(BasePage):
    """
    Strona główna``
    """

    def accept_cookies(self):
        self.driver.find_element(*Locators.COOKIES_ACCEPT).click()

    def go_to_sale_page(self):
        """Klika w przycisk SALE"""
        self.driver.find_element(*Locators.SALE).click()
        return

    def _verify_page(self):
        """
        Weryfikacja strony głównej
        """
