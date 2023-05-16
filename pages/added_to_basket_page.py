from pages.base_page import BasePage
from Locators.Locators import Locators

class AddedToBasket(BasePage):

    def go_to_basket(self):
        """Go to basket"""
        self.driver.find_element(*Locators.GO_TO_BASKET).click()
        return

    def continue_shopping(self):
        """Continue shopping"""
        self.driver.find_element(*Locators.CONTINUE_SHOPPING).click()
