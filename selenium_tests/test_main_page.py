from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.locators import BasePageLocators
from .pages.locators import CalendarPageLocators
from .pages.locators import Link
import pytest

def test_positive_click_submit(browser):
    page = BasePage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.NAME)
    page.input_field(*BasePageLocators.NAME, "Иван")
    page.input_field(*BasePageLocators.EMAIL, "ivan_ivanov@gmail.com")
    page.input_field(*BasePageLocators.PHONE, "89231166754")
    page.input_field(*BasePageLocators.SUBJECT, "Сообщение")
    page.input_field(*BasePageLocators.DESCRIPTION, "ААААААААААААААААААААААААААААААААААААААААААААААААААААААААА")
    page.click_button(*BasePageLocators.SUBMITCONTACT)
    page.should_be_element(*BasePageLocators.TITLE_SUCCESS)

def test_negative_null_name(browser):
    page = MainPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.EMAIL)
    page.input_field(*BasePageLocators.EMAIL, "ivan_ivanov@gmail.com")
    page.input_field(*BasePageLocators.PHONE, "89231166754")
    page.input_field(*BasePageLocators.SUBJECT, "Сообщение")
    page.input_field(*BasePageLocators.DESCRIPTION, "ААААААААААААААААААААААААААААААААААААААААААААААААААААААААА")
    page.click_button(*BasePageLocators.SUBMITCONTACT)
    page.message_is_appeared_text_name_null(*BasePageLocators.MESSAGE_ERROR)
        
def test_delete_symbols(browser):
    page = MainPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.DESCRIPTION)
    page.input_field(*BasePageLocators.DESCRIPTION, "А")
    page.delete_symbols(*BasePageLocators.DESCRIPTION)
    page.checking_empty_field(*BasePageLocators.DESCRIPTION)
      
def test_map_exist(browser):
    page = MainPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.MAP)
    page.should_be_element(*BasePageLocators.MAP)

def test_click_bookthisroom(browser):
    page = MainPage(browser, Link.LINK)
    page.open()
    page.scroll_element(*BasePageLocators.BOOK_THIS_ROOM)
    page.click_button(*BasePageLocators.BOOK_THIS_ROOM)
    page.should_be_element(*CalendarPageLocators.FIRSTNAME)
    page.should_be_element(*CalendarPageLocators.LASTNAME)
    page.should_be_element(*CalendarPageLocators.EMAIL)
    page.should_be_element(*CalendarPageLocators.PHONE)
    

    

    
