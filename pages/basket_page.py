from pages.base_page import BasePage
from Locators.Locators import Locators


class BasketPage(BasePage):

    def number_of_products(self):
        """Number of products in basket"""
        return self.driver.find_element(*Locators.NUMBER_OF_PRODUCTS)

    def available_icon(self):
        """Icon"""
        return self.driver.find_element(*Locators.ICON)

    def remove_products(self):
        """Remove products from basket"""
        return self.driver.find_element(*Locators.REMOVE_PRODUCT).click()


    def empty_basket(self):
        """Basket is empty"""
        self.driver.find_element(*Locators.EMPTY_BASKET).click()
        return


    def currency_settings(self):
        """Open currency settings"""
        return self.driver.find_element(*Locators.CURRENCY_SETTINGS).click()

    def change_currency_settings(self):
        """Change currency settings"""
        return self.driver.find_element(*Locators.CHANGE_CURRENCY_SETTINGS).click()

    def change_currency(self):
        """Change currency"""
        return self.driver.find_element(*Locators.CHANGE_CURRENCY).click()

    def confirm_currency(self):
        """Confirm currency"""
        return self.driver.find_element(*Locators.CONFIRM_CURRENCY_CHANGE).click()

    def final_amount(self):
        """Get final amount"""
        return self.driver.find_element(*Locators.TOTAL_PAY_ELEMENT)

    def price_of_product(self):
        """Get price of product"""
        return self.driver.find_elements(*Locators.PRICES)

    def shipping_cost(self):
        """Get shipping costs"""
        return self.driver.find_element(*Locators.SHIPPING_COST)
