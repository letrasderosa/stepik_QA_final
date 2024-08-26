
class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_element_visible(self, how, what):
        try:
            element = self.driver.find_element(by=how, value=what)
            return element.is_displayed()
        except StaleElementReferenceException:
            return False