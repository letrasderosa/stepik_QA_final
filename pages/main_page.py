from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not present"
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not present"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK)
        # assert self.is_element_present(By.CSS_SELECTOR, "#registration_link"), "Login link is not present"