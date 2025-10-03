from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class AccountPage:
    ORDER_HISTORY_BUTTON = [By. XPATH, './/a[text() = "История заказов"]']
    EXITE_BUTTON = [By. XPATH, './/button[text() = "Выход"]']

    def __init__(self, driver):
        super().__init__(driver)

    