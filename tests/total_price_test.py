from pages.basket_page import BasketPage
from pages.added_to_basket import AddedToBasket
from pages.product_page import ProductPage
from pages.sale_page import SalePage
from tests.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Locators.Locators import Locators

class TotalPriceTest(BaseTest):
    def test_basket_total_price(self):
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

        #Continue shopping
        added_to_basket_page_object = AddedToBasket(self.driver)
        added_to_basket_page_object.continue_shopping()

        #Add another size
        product_page_object.choose_size2()

        # Add to basket
        product_page_object.add_to_basket()

        # Go to basket
        added_to_basket_page_object.go_to_basket()

        #Test - items in basket plus delivery costs = final amount

        # Find final amount of basket
        basket_page_object = BasketPage(self.driver)
        total_pay_element = basket_page_object.final_amount()
        # Get final amount and replace some characters
        total_pay_text = total_pay_element.text.replace('Total to pay:\n', '').strip().replace(',', '.').replace('€', '')
        print("Final amount:", total_pay_text)

        # Find elements with prices
        prices = basket_page_object.price_of_product()

        # Sum all elements in basket
        total_price = 0
        for price in prices:
            # Get the price text and remove the currency sign and any spaces
            price_text = price.text.strip().replace("€", "").replace(" ", "").replace(",", ".")
            # If the text is not empty, convert to a floating point number and add to the total
            if price_text:
                total_price += float(price_text.replace(",", "."))

        # Show amounts for items in basket
        print("Total amount of products:", total_price)

        # Find shipping costs
        shipping_cost_element = basket_page_object.shipping_cost()

        # Get shipping costs
        shipping_cost_text = shipping_cost_element.text.strip().replace("€", "").replace(",", ".")
        print("Delivery cost:", shipping_cost_text)

        # Add shipping costs to items from basket
        total_sum_with_shipping = total_price + float(shipping_cost_text)

        #Show total amount of items from basket and shipping costs
        print("Total amount of products with delivery cost:", total_sum_with_shipping)

        assert round(total_sum_with_shipping, 2) == round(float(total_pay_text.replace(",", "")), 2), f"Wrong basket sum {total_pay_element} (expected{total_sum_with_shipping})"

    def click_close(self):
        pass
