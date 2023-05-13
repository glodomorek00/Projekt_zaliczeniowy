from pages.sale_page import SalePage
from tests.base_test import BaseTest
from pages.product_page import ProductPage
from Locators.Locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPageTest(BaseTest):
    def test_first_product(self):
        # Go to new page - SALE
        self.home_page_object.go_to_sale_page()

        # Apply filters
        sale_page_object = SalePage(self.driver)
        sale_page_object.get_filtered_products()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(Locators.FILTER_LIST_CONTENT))

        # Select first product
        sale_page_object.get_first_product()
        wait.until(EC.visibility_of_element_located(Locators.ADD_TO_BASKET))

        # Scroll to element
        self.driver.execute_script("window.scrollBy(0, 2500)")
        wait.until(EC.visibility_of_element_located(Locators.GENDER_ELEMENT))

        # Define gender
        product_page_object = ProductPage(self.driver)
        gender_element = product_page_object.gender_element()

        # Check gender of product
        gender_text = gender_element.text.lower()
        print("Text:", gender_text)
        assert gender_text == "women's", f"Wrong gender: {gender_text}"


    def click_close(self):
        pass
