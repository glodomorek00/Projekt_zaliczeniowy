from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import Locators
from tests.base_test import BaseTest
from pages.basket_page import BasketPage
from pages.sale_page import SalePage
from pages.product_page import ProductPage
from pages.added_to_basket_page import AddedToBasket
from pages.empty_basket_page import EmptyBasketPage


class BasketTest(BaseTest):

    def test_basket(self):
        # Go to new page - SALE
        self.home_page_object.go_to_sale_page()

        #Apply filters
        sale_page_object = SalePage(self.driver)
        sale_page_object.get_filtered_products()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(Locators.FILTER_LIST_CONTENT))

        #Select first product
        sale_page_object.get_first_product()

        # Choose size
        product_page_object = ProductPage(self.driver)
        product_page_object.choose_size()

        # Add to basket
        product_page_object.add_to_basket()

        # Go to basket
        added_to_basket_page_object = AddedToBasket(self.driver)
        added_to_basket_page_object.go_to_basket()

        # Check if product was added to basket
        basket_page_object = BasketPage(self.driver)
        product = basket_page_object.number_of_products()
        product_value = product.get_attribute('value')

        print("Number of products in basket:", product_value)

        assert product_value == "1", f"Wrong quantity: {product_value}"

        # Find element with icon
        icon = basket_page_object.available_icon()

        # Check if icon is available
        assert icon.is_displayed(), "Icon is not available"

        # Remove the products from basket
        basket_page_object.remove_products()

        # Wait until products are removed
        wait.until(EC.visibility_of_element_located(Locators.EMPTY_BASKET))

        # Check if products are removed
        empty_basket_page_object = EmptyBasketPage(self.driver)
        no_products_message = empty_basket_page_object.empty_basket()
        no_products_message_text = no_products_message.text
        print("Tekst:", no_products_message_text)
        assert no_products_message.is_displayed(),"Text 'Your basket is empty.' is not visble on the page"


    def click_close(self):
        pass
