from selenium.webdriver.common.by import By

class Locators:
    # Locators - Home Page:
    COOKIES_ACCEPT = (By.XPATH, '//span[@class="ck_dsclr__btn_v2"]')
    SALE = (By.XPATH, '//a[@href="/eng_m_SALE-722.html"]')

    #Locators - Sale Page:
    FILTR_SORT = (By.XPATH, '//button[@class="filters-btn__item"]')
    MORE_SIZE = (By.XPATH, '//span[@class="--show"]')
    CHOOSE_SIZE = (By.XPATH, '//label[@for="filter_sizes_1311"]')
    CHOOSE_GENDER_LIST = (By.XPATH, '//a[@data-id="filter_traits26"]')
    CHOOSE_GENDER = (By.XPATH, '//label[@for="filter_traits26_34"]')
    APPLY_FILTERS = (By.XPATH, '//button[@class="btn d-block"]')
    FIRST_ELEMENT = (By.XPATH, "//a[@class='product__name'][1]")
    SALE_PAGE = (By.XPATH, '//h1[@class="big_label"]')
    FILTER_LIST_CONTENT = (By.XPATH, '//div[@class="filter_list_content"]')

    #Locators - Product Page:
    CHOOSE_SIZE_FIRST_ELEMENT = (By.XPATH, '//a[@href="/product-eng-4049-Puma-Suede-Mayu-ST-Wns-WHITE-38327301.html?selected_size=1033"]')
    CHOOSE_SIZE_SECOND_ELEMENT = (By.XPATH, '//a[@href="/product-eng-4049-Puma-Suede-Mayu-ST-Wns-WHITE-38327301.html?selected_size=1034"]')
    ADD_TO_BASKET = (By.XPATH, '//button[@title="Add 1 item to shopping basket"]')
    GENDER_ELEMENT = (By.XPATH, '//span[@class="dictionary__value_txt"]')

    #Locators -Added to basket:
    GO_TO_BASKET = (By.XPATH, '//a[@class="btn --solid --medium added__button --add"]')
    CONTINUE_SHOPPING = (By.XPATH, '//a[@class="btn --medium added__button --close mt-1 mt-sm-0 ml-sm-2"]')

    #Locators for basket - number of products in basket:
    NUMBER_OF_PRODUCTS = (By.CSS_SELECTOR, '[value="1"]')

    #Locators for basket - icon:
    ICON = (By.XPATH, '//span[@class="badge badge-info"]')

    #Locators for basket - remove product:
    REMOVE_PRODUCT = (By.XPATH, '//span[@class="remove__button --desktop btn d-none d-md-inline-block icon-remove"]')

    #Locators for basket - empty basket:
    EMPTY_BASKET = (By.XPATH, '//h3[contains(text(),"Your basket is empty.")]')

    #Locators for basket - currency test:
    CURRENCY_SETTINGS = (By.ID, "menu_settings_currency")
    CHANGE_CURRENCY_SETTINGS = (By.ID, "menu_settings_curr")
    CHANGE_CURRENCY = (By.XPATH, '//option[@value="USD"]')
    CONFIRM_CURRENCY_CHANGE = (By.XPATH, '//button[@class="btn --solid --large"]')

    #Locators for basket - final amount:
    TOTAL_PAY_ELEMENT = (By.XPATH, '//div[@class="basketedit_total_summary"]')

    #Locators for basket - amounts of particular products:
    PRICES = (By.XPATH, '//span[@class="basket__sum"]')

    #Locators for basket - total price test:
    SHIPPING_COST = (By.XPATH, '//strong[@class="plus_sign"]')