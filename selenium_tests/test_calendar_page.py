from .pages.base_page import BasePage
from .pages.calendar_page import CalendarPage
from .pages.locators import BasePageLocators
from .pages.locators import CalendarPageLocators
from .pages.locators import Link
import pytest
import time

def test_click_cancel(browser):
    page = CalendarPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.BOOK_THIS_ROOM)
    page.click_button(*BasePageLocators.BOOK_THIS_ROOM)
    page.click_button(*CalendarPageLocators.CANCEL)
    page.no_should_be_element(*CalendarPageLocators.CANCEL)
   
    
def test_positive_click_submit(browser):
    page = CalendarPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.BOOK_THIS_ROOM)
    page.click_button(*BasePageLocators.BOOK_THIS_ROOM)
    page.input_field(*CalendarPageLocators.FIRSTNAME, "Иван")
    page.input_field(*CalendarPageLocators.LASTNAME, "Иван")
    page.input_field(*CalendarPageLocators.EMAIL, "ivan_ivanov@gmail.com")
    page.input_field(*CalendarPageLocators.PHONE, "89231166754")
    page.click_button(*CalendarPageLocators.BUTTON_NEXT)
    page.selected_date(browser, *CalendarPageLocators.DATE_ONE, *CalendarPageLocators.DATE_TWO)
    page.click_button(*CalendarPageLocators.BUTTON_BOOK)
    page.should_be_element(*CalendarPageLocators.CLOSE)

def test_click_close_alert(browser):
    page = CalendarPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.BOOK_THIS_ROOM)
    page.click_button(*BasePageLocators.BOOK_THIS_ROOM)
    page.input_field(*CalendarPageLocators.FIRSTNAME, "Иван")
    page.input_field(*CalendarPageLocators.LASTNAME, "Иван")
    page.input_field(*CalendarPageLocators.EMAIL, "ivan_ivanov@gmail.com")
    page.input_field(*CalendarPageLocators.PHONE, "89231166754")
    page.click_button(*CalendarPageLocators.BUTTON_NEXT)
    page.selected_date(browser, *CalendarPageLocators.DATE_A, *CalendarPageLocators.DATE_B)
    page.click_button(*CalendarPageLocators.BUTTON_BOOK)
    page.click_button(*CalendarPageLocators.CLOSE)
    page.no_should_be_element(*CalendarPageLocators.FIRSTNAME)

def test_early_selected_dates(browser):
    page = CalendarPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.BOOK_THIS_ROOM)
    page.click_button(*BasePageLocators.BOOK_THIS_ROOM)
    page.input_field(*CalendarPageLocators.FIRSTNAME, "Иван")
    page.input_field(*CalendarPageLocators.LASTNAME, "Иван")
    page.input_field(*CalendarPageLocators.EMAIL, "ivan_ivanov@gmail.com")
    page.input_field(*CalendarPageLocators.PHONE, "89231166754")
    page.click_button(*CalendarPageLocators.BUTTON_NEXT)
    page.selected_date(browser, *CalendarPageLocators.DATE_ONE, *CalendarPageLocators.DATE_TWO)
    page.click_button(*CalendarPageLocators.BUTTON_BOOK)
    page.message_is_appeared_text_error_dates(*CalendarPageLocators.MESSAGE_ERROR)

def test_early_part_selected_dates(browser):
    page = CalendarPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.BOOK_THIS_ROOM)
    page.click_button(*BasePageLocators.BOOK_THIS_ROOM)
    page.input_field(*CalendarPageLocators.FIRSTNAME, "Иван")
    page.input_field(*CalendarPageLocators.LASTNAME, "Иван")
    page.input_field(*CalendarPageLocators.EMAIL, "ivan_ivanov@gmail.com")
    page.input_field(*CalendarPageLocators.PHONE, "89231166754")
    page.click_button(*CalendarPageLocators.BUTTON_NEXT)
    page.selected_date(browser, *CalendarPageLocators.DATE_A, *CalendarPageLocators.DATE_C)
    page.click_button(*CalendarPageLocators.BUTTON_BOOK)
    page.message_is_appeared_text_error_dates(*CalendarPageLocators.MESSAGE_ERROR)

 





    

    
