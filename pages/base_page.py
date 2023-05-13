class BasePage:
    """
    Base class for every page.
    It will not have instances. Actual pages will inherit from it.
    """
    def __init__(self, driver):
        self.driver = driver #driver is a part of Base Page
        self._verify_page() #each page will be verified automatically

    def _verify_page(self): # method is private, not public
        pass