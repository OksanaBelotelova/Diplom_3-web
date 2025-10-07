from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class AccountPage(BasePage):
    
    PROFILE_BUTTON = [By. XPATH, './/a[text() = "Профиль"]']
    ORDERS_HISTORY_BUTTON = [By. XPATH, './/a[text() = "История заказов"]']
    LOGOUT_BUTTON = [By. XPATH, './/button[text() = "Выход"]']
    LOGIN_BUTTON = [By. XPATH, './/button[text() = "Войти"]']
    ORDERS_LOADING = [By.XPATH, '//div[text() = "Загрузка..."]']
    USER_LAST_ORDER_ID = [
        By.XPATH, './/ul[contains(@class, "OrderHistory_profileList")]/li[last()]/a/div[contains(@class, "OrderHistory_textBox")]/p[1]']


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Подожди пока загрузится страница')
    def wait_until_page_loaded(self):
        self.wait_until_visible(self.PROFILE_BUTTON)

    @allure.step('Перейди в секцию "История заказов"')
    def click_orders_history(self):
        self.find_element(self.ORDERS_HISTORY_BUTTON).click()
    
    @allure.step('Нажми на кнопку "Выход"')
    def click_logout_button(self):
        self.find_element(self.LOGOUT_BUTTON).click()
        self.wait_until_clickable(self.LOGIN_BUTTON, time=10)

    @allure.step('Проверь id заказа')
    def get_user_last_order_id(self):
        self.wait_until_not_presence(self.ORDERS_LOADING)
        return self.find_element(self.USER_LAST_ORDER_ID).text
