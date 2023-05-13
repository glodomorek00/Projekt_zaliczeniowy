from pages.base_page import BasePage
from Locators.Locators import Locators

class SalePage(BasePage):

    def sale_page(self):
        """Get Sale page text"""
        return self.driver.find_element(*Locators.SALE_PAGE)

    def get_filtered_products(self):
        """Filter by size '37.5' and gender 'Women's'"""
        self.driver.find_element(*Locators.FILTR_SORT).click()
        self.driver.find_element(*Locators.MORE_SIZE).click()
        self.driver.find_element(*Locators.CHOOSE_SIZE).click()
        self.driver.find_element(*Locators.CHOOSE_GENDER_LIST).click()
        self.driver.find_element(*Locators.CHOOSE_GENDER).click()
        self.driver.find_element(*Locators.APPLY_FILTERS).click()

    def get_filter_content(self):
        """Get filter content"""
        return self.driver.find_elements(*Locators.FILTER_LIST_CONTENT)

    def get_first_product(self):
        """Select first element"""
        self.driver.find_element(*Locators.FIRST_ELEMENT).click()
        return


