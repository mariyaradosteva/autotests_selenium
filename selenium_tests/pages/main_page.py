from .base_page import BasePage
from .locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def message_is_appeared_text_name_null(self, how, what):
        assert self.is_appeared_text_name_null(how, what), "Message is not corrected"

    def is_appeared_text_name_null(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element((how, what), "Name may not be blank"))
        except TimeoutException:
            return False
        return True

    