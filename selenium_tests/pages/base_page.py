from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.webdriver.common.keys import Keys


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
 
    def input_field(self, how, what, text):
        inp =  self.browser.find_element(how, what)
        inp.send_keys(text)

    def click_button(self, how, what):
        cl = self.browser.find_element(how, what)
        cl.click()
    
    def scroll_element(self, how, what):
        scr = self.browser.find_element(how, what)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", scr)

    def should_be_element(self, how, what):
        assert self.is_element_present(how, what), "Element is not presented"   
       
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
 
    def delete_symbols(self, how, what):
        scr = self.browser.find_element(how, what)
        scr.send_keys(Keys.BACKSPACE)

    def checking_empty_field(self, how, what):
        scr = self.browser.find_element(how, what)
        assert scr.text == "", "The field is not empty"

    def no_should_be_element(self, how, what):
        assert self.is_not_element_present(how, what), "Element is presented"   
        
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

                                                              
        