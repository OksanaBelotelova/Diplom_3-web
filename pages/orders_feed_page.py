from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class OrdersFeed(BasePage):

    ORDER = [By. XPATH, './/li[contains(@class, "OrderHistory_listItem__")]']
    ORDER_DETAILS_POPUP = [By. XPATH, './/div[contains(@class, "Modal_modal__container")]']
    
    def __init__(self, driver):
        super().__init__(driver)



