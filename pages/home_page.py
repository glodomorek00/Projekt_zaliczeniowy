from pages.base_page import BasePage
from pages.sale_page import SalePage
from Locators.Locators import Locators

class FirstPage(BasePage): #Nadpisujemy BasePage, ale ten sam init! wszystko co wpiszemy w ten plik to się wywoła co jest w tym pliku
    """
    Strona główna``
    """

    def accept_cookies(self):
        self.driver.find_element(*Locators.COOKIES_ACCEPT).click()

    def go_to_sale_page(self):
        """Klika w przycisk SALE"""
        self.driver.find_element(*Locators.SALE).click()
        return

    # def get_filtered_products(self):
    #     """Filtruje po rozmiarze 37.5 oraz płci kobieta"""
    #     self.driver.find_element(*Locators.FILTR_SORT).click()
    #     self.driver.find_element(*Locators.MORE_SIZE).click()
    #     sleep(5)
    #     self.driver.find_element(*Locators.CHOOSE_SIZE).click()
    #     self.driver.find_element(*Locators.CHOOSE_SEX_LIST).click()
    #     self.driver.find_element(*Locators.CHOOSE_SEX).click()
    #     sleep(5)
    #     self.driver.find_element(*Locators.APPLY_FILTERS).click()
    #     sleep(5)

    # def get_first_product(self):
    #     """Kliknij na pierwszy element"""
    #     self.driver.find_element(*Locators.FIRST_ELEMENT).click()

        # Kliknij
        # Zwroc kolejna stronę
    #
    # def choose_size(self):
    #     return self.driver.find_element(*Locators.CHOOSE_SIZE_FIRST_ELEMENT)
    #
    # def add_to_basket(self):
    #     return self.driver.find_element(*Locators.ADD_TO_BASKET)
    #
    # def go_to_basket(self):
    #     return self.driver.find_element(*Locators.GO_TO_BASKET)
    #
    # def number_of_products(self):
    #     return self.driver.find_element(*Locators.NUMBER_OF_PRODUCTS)
    #
    # def available_icon(self):
    #     return self.driver.find_element(*Locators.ICON)
    #
    # def remove_products(self):
    #     return self.driver.find_element(*Locators.REMOVE_PRODUCT)

    # def empty_basket(self):
    #     return self.driver.find_element(*Locators.EMPTY_BASKET)
    #
    # def total_amount(self):
    #     return self.driver.find_element(*Locators.TOTAL_PAY_ELEMENT)
    #
    # def Hprices(self):
    #     return self.driver.find_element(*Locators.PRICES)


    def _verify_page(self):  # _ to oznacza, że metoda jest prywatna, a nie publiczna, sama strona bedzie ja uruchamiac
        """
        Weryfikacja strony głównej
        """
        pass



