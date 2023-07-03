from .base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalendarPage(BasePage):

    def selected_date(self, browser, howA, whatA, howB, whatB):
        source_element = self.browser.find_element(howA, whatA)
        target_element = self.browser.find_element(howB, whatB)
        k = self.calculating_first_date(whatA)
        action = ActionChains(browser)
        action.click_and_hold(k).move_to_element(source_element).move_to_element(target_element).release().perform()

    def calculating_first_date(self, whatA):
        if int(whatA[53]) - 1 == 0:
            return self.browser.find_element(By.CSS_SELECTOR, ".rbc-month-row:nth-child(" + str(int(whatA[25]) - 1) + ") .rbc-date-cell:nth-child(" + str(7) + ")")
        else:
            return self.browser.find_element(By.CSS_SELECTOR, ".rbc-month-row:nth-child(" + whatA[25] + ") .rbc-date-cell:nth-child(" + str(int(whatA[53]) - 1) + ")")

    def message_is_appeared_text_error_dates(self, how, what):
        assert self.is_appeared_text_error_dates(how, what), "Message is not corrected"

    def is_appeared_text_error_dates(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element((how, what), "The room dates are either invalid or are already booked for one or more of the dates that you have selected."))
        except TimeoutException:
            return False
        return True