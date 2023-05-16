from selenium.webdriver.common.by import By

class Locators:
    # Locators - Home Page:
    COOKIES_ACCEPT = (By.XPATH, '//span[@class="ck_dsclr__btn_v2"]')
    SALE = (By.XPATH, '//a[@href="/eng_m_SALE-722.html"]')

    #Locators - Sale Page:
    FILTR_SORT = (By.XPATH, '//button[@class="filters-btn__item"]')
    SHOW_ALL = (By.XPATH, '//span[@class="--show"]')
    CHOOSE_SIZE = (By.XPATH, '//label[@for="filter_sizes_825"]')
    CHOOSE_GENDER_LIST = (By.XPATH, '//a[@data-id="filter_traits26"]')
    CHOOSE_GENDER = (By.XPATH, '//label[@for="filter_traits26_34"]')
    APPLY_FILTERS = (By.XPATH, '//button[@class="btn d-block"]')
    FIRST_ELEMENT = (By.XPATH, '//a[@class="product__name"][1]')
    SALE_PAGE = (By.XPATH, '//h1[@class="big_label"]')
    FILTER_LIST_CONTENT = (By.XPATH, '//div[@class="filter_list_content"]')
    ORGINAL_PRICE_ELEMENT = (By.ID, "projector_price_maxprice")
    DISCOUNTED_PRICE_ELEMENT = (By.ID, "projector_price_value")

    #Locators - Product Page:
    CHOOSE_SIZE_FIRST_ELEMENT = (By.XPATH, '//a[@class="select_button"]')
    CHOOSE_SIZE_SECOND_ELEMENT = (By.XPATH, '//a[@href="/product-eng-4733-Converse-ARCHIVE-SKATE-CHUCK-70-170925C.html?selected_size=943"]')
    ADD_TO_BASKET = (By.XPATH, '//button[@title="Add 1 item to shopping basket"]')
    GENDER_ELEMENT = (By.XPATH, '//div[@class="dictionary__param mb-3"][2]')
    ELEMENT = (By.XPATH, '//span[@class="dictionary__value_txt"]')
    DISCOUNT_ELEMENT = (By.ID, "projector_price_yousave")

    #Locators -Added to basket:
    GO_TO_BASKET = (By.XPATH, '//a[@class="btn --solid --medium added__button --add"]')
    CONTINUE_SHOPPING = (By.XPATH, '//a[@class="btn --medium added__button --close mt-1 mt-sm-0 ml-sm-2"]')

    #Locators - Basket Page:
    NUMBER_OF_PRODUCTS = (By.CSS_SELECTOR, '[value="1"]')
    ICON = (By.XPATH, '//span[@class="badge badge-info"]')
    REMOVE_PRODUCT = (By.XPATH, '//span[@class="remove__button --desktop btn d-none d-md-inline-block icon-remove"]')
    EMPTY_BASKET = (By.XPATH, '//h3[contains(text(),"Your basket is empty.")]')
    CURRENCY_SETTINGS = (By.ID, "menu_settings_currency")
    CHANGE_CURRENCY_SETTINGS = (By.ID, "menu_settings_curr")
    CHANGE_CURRENCY = (By.XPATH, '//option[@value="USD"]')
    CONFIRM_CURRENCY_CHANGE = (By.XPATH, '//button[@class="btn --solid --large"]')
    TOTAL_PAY_ELEMENT = (By.XPATH, '//div[@class="basketedit_total_summary"]')
    PRICES = (By.XPATH, '//span[@class="basket__sum"]')
    SHIPPING_COST = (By.XPATH, '//strong[@class="plus_sign"]')
