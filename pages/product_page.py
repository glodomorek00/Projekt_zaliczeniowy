from pages.base_page import BasePage
from Locators.Locators import Locators

class ProductPage(BasePage):

    def choose_size(self):
        """Choose size for first element"""
        self.driver.find_element(*Locators.CHOOSE_SIZE_FIRST_ELEMENT).click()

    def gender_element(self):
        """Locate gender elemet"""
        return self.driver.find_element(*Locators.GENDER_ELEMENT)

    def choose_size2(self):
        """Choose size for second element"""
        self.driver.find_element(*Locators.CHOOSE_SIZE_SECOND_ELEMENT).click()


    def add_to_basket(self):
        """Add products to basket"""
        self.driver.find_element(*Locators.ADD_TO_BASKET).click()

