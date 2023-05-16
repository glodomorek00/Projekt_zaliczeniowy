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


        # Check if discount is calculated for product
        product_page_object = ProductPage(self.driver)
        discount_element = product_page_object.discount_element()
        discount_element_text = discount_element.text
        print("Discount:", discount_element_text)

        if discount_element.is_displayed():
            # Amount without discount
            orginal_price_element = product_page_object.orginal_price_element()
            original_price = float(orginal_price_element.text.replace('€', '').replace(',', '.'))
            discounted_price_element = product_page_object.discounted_price_element()

            # Amount after discount
            discounted_price = float(discounted_price_element.text.replace('€', '').replace(',', '.'))

            # Calculate amount of discount
            discount_amount = original_price - discounted_price
            assert discount_amount > 0, "Zniżka nie została naliczona."

            print(f"Discount calculated. The amount of discount is: €{discount_amount}")
        else:
            print("Discount is not calculated.")

        # Scroll to element
        self.driver.execute_script("window.scrollBy(0, 2500)")
        wait.until(EC.visibility_of_element_located(Locators.ELEMENT))

        # Define gender
        gender_element = product_page_object.gender_element()

        # Check gender of product
        gender_text = gender_element.text.lower().strip()
        print("Text:", gender_text)
        if "women's" in gender_text:
            print("Gender is correct: women's")
        else:
            raise AssertionError(f"Wrong gender: {gender_text}")



    def click_close(self):
        pass
