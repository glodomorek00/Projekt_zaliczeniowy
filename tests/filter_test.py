from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.sale_page import SalePage
from tests.base_test import BaseTest
from time import sleep
from Locators.Locators import Locators

#TC1

class FilterTest(BaseTest):
    def test_filtering(self):
        # Go to new page - SALE
        self.home_page_object.go_to_sale_page()

        # Check SALE page
        sale_page_object = SalePage(self.driver)
        sale = sale_page_object.sale_page()
        sale_text = sale.text.strip()
        assert "SALE" in sale_text, "Not on sale page"

        # Apply filters
        sale_page_object = SalePage(self.driver)
        sale_page_object.get_filtered_products()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(Locators.FILTER_LIST_CONTENT))

        # Get filter list content
        filter_list_content = sale_page_object.get_filter_content()

        for item in filter_list_content:

            # Check filtered size and gender
            list_text = item.text
            print("Applied Filters:", list_text)
            assert "37.5" in list_text
            assert "Women's" in list_text

         # Refresh page
        self.driver.refresh()
        sleep(10)

        # Check if active filters are the same as applied filters
        assert "37.5" in list_text
        assert "Women's" in list_text

    def tearDown(self):
        self.driver.quit()

