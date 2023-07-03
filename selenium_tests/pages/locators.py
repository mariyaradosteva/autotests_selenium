from selenium.webdriver.common.by import By

class Link():
    
    LINK = "https://automationintesting.online/"

class BasePageLocators():

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    SUBJECT = (By.ID, "subject")
    DESCRIPTION = (By.ID, "description")
    SUBMITCONTACT = (By.ID, "submitContact")
    BOOK_THIS_ROOM = (By.CSS_SELECTOR, ".openBooking")
    TITLE_SUCCESS = (By.CSS_SELECTOR, ".contact h2")
    MESSAGE_ERROR = (By.CSS_SELECTOR, ".alert-danger :nth-child(1)")
    MAP = (By.CSS_SELECTOR, ".pigeon-click-block :nth-child(1)")

class CalendarPageLocators():

    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    PHONE = (By.NAME, "phone")
    BUTTON_BOOK = (By.CSS_SELECTOR, ".hotel-room-info .btn-outline-primary")
    BUTTON_CANCEL = (By.CSS_SELECTOR, ".hotel-room-info .btn-outline-danger")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".rbc-btn-group :nth-child(3)")
    CANCEL = (By.CSS_SELECTOR, ".hotel-room-info .btn-outline-danger")
    DATE_ONE = (By.CSS_SELECTOR, ".rbc-month-row:nth-child(2) .rbc-date-cell:nth-child(2)")
    DATE_TWO = (By.CSS_SELECTOR, ".rbc-month-row:nth-child(2) .rbc-date-cell:nth-child(3)")
    CLOSE = (By.XPATH, '//button[text()="Close"]')
    MESSAGE_ERROR = (By.CSS_SELECTOR, ".alert-danger")
    DATE_A = (By.CSS_SELECTOR, ".rbc-month-row:nth-child(3) .rbc-date-cell:nth-child(2)")
    DATE_B = (By.CSS_SELECTOR, ".rbc-month-row:nth-child(3) .rbc-date-cell:nth-child(3)")
    DATE_C = (By.CSS_SELECTOR, ".rbc-month-row:nth-child(3) .rbc-date-cell:nth-child(4)")
    
    