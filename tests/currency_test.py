from pages.basket_page import BasketPage
from pages.added_to_basket_page import AddedToBasket
from pages.product_page import ProductPage
from pages.sale_page import SalePage
from tests.base_test import BaseTest
from Locators.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CheckCurrencyTest(BaseTest):
    def test_currency(self):
        # Go to new page - SALE
        self.home_page_object.go_to_sale_page()

        # Apply filters
        sale_page_object = SalePage(self.driver)
        sale_page_object.get_filtered_products()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(Locators.FILTER_LIST_CONTENT))

        # Select first product
        sale_page_object.get_first_product()

        # Choose size
        product_page_object = ProductPage(self.driver)
        product_page_object.choose_size()

        # Add to basket
        product_page_object.add_to_basket()

        # Go to basket
        add_to_basket_page_object = AddedToBasket(self.driver)
        add_to_basket_page_object.go_to_basket()

        # Change currency
        basket_page_object = BasketPage(self.driver)
        basket_page_object.currency_settings()
        basket_page_object.change_currency_settings()
        basket_page_object.change_currency()
        basket_page_object.confirm_currency()

        # Check if the currency was changed
        total_pay_element = basket_page_object.final_amount()

        #Change the currency to text
        total_pay_text = total_pay_element.text
        print("Final amount:", total_pay_text)
        assert "$" in total_pay_text, f"Amount doesn't contain $: {total_pay_text}"


    def click_close(self):
        pass
