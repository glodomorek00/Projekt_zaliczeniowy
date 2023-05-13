from pages.base_page import BasePage
from Locators.Locators import Locators

class EmptyBasketPage(BasePage):

    def empty_basket(self):
        return self.driver.find_element(*Locators.EMPTY_BASKET)