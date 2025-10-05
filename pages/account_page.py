from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class AccountPage(BasePage):
    PROFILE_BUTTON = [By. XPATH, './/a[text() = "Профиль"]']
    ORDERS_HISTORY_BUTTON = [By. XPATH, './/a[text() = "История заказов"]']
    LOGOUT_BUTTON = [By. XPATH, './/button[text() = "Выход"]']
    NAME_FIELD = [By. XPATH, './/input[@name = "Name"]']
    LOGIN_BUTTON = [By. XPATH, './/button[text() = "Войти"]']
    def __init__(self, driver):
        super().__init__(driver)

    def wait_until_page_loaded(self):
        self.wait_until_visible(self.PROFILE_BUTTON)
        
    def click_orders_history(self):
        self.find_element(self.ORDERS_HISTORY_BUTTON).click()

    def click_logout_button(self):
        self.find_element(self.LOGOUT_BUTTON).click()
        self.wait_until_clickable(self.LOGIN_BUTTON, time = 10)

        