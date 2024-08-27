# from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    # def is_element_visible(self, how, what):
    #     try:
    #         element = self.browser.find_element(by=how, value=what)
    #         return element.is_displayed()
    #     except StaleElementReferenceException:
    #         return False
    #
    # def is_element_invisible(self, how, what):
    #     try:
    #         element = self.browser.find_element(by=how, value=what)
