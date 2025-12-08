from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from data import AuthCredentials


class LoginPage(BasePage):

    EMAIL_FIELD = [By. XPATH, './/input[@name = "name"]']
    PASSWORD_FIELD = [By. XPATH, './/input[@name = "Пароль"]']
    LOGIN_BUTTON = [By. XPATH, './/button[text() = "Войти"]']
    RESTORE_PASSWORD_BUTTON = [By. XPATH, './/a[@href = "/forgot-password"]']
    RESTORE_BUTTON = [By. XPATH, './/button[text() = "Восстановить"]']
    SHOW_HIDE_BUTTON = [By. XPATH,
                        './/div[@class="input__icon input__icon-action"]']
    NEW_PASSWORD_FIELD_ACTIVE_WRAPPER = [By. XPATH,
                                         './/label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]']


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликни "Восстановить пароль"')
    def click_restore_password_button(self):
        self.find_element(self.RESTORE_PASSWORD_BUTTON).click()

    @allure.step('Введи имейл')
    def input_email(self, email):
        self.find_element(self.EMAIL_FIELD).send_keys(email)

    @allure.step('Нажми на "Восстановить"')
    def click_restore_button(self):
        self.wait_until_clickable(self.RESTORE_BUTTON, time=10)
        self.find_element(self.RESTORE_BUTTON).click()
        self.wait_until_clickable(self.SHOW_HIDE_BUTTON, time=10)

    @allure.step('Нажми на кнопку "Показать/скрыть пароль"')
    def click_show_password_button(self):
        self.find_element(self.SHOW_HIDE_BUTTON).click()

    @allure.step('Проверь что поле подсвечено')
    def get_active_new_password_field_wrapper(self):
        return self.find_element(self.NEW_PASSWORD_FIELD_ACTIVE_WRAPPER)

    @allure.step('Введи пароль')
    def input_password(self, password):
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step('Кликни на кнопку "Войти"')
    def click_login_button(self):
        self.find_element(self.LOGIN_BUTTON).click()

    @allure.step('Выполни вход на сайт')
    def submit_login_form(self):
        auth_credentials = AuthCredentials()
        self.click_login_account_button()
        self.input_email(auth_credentials.registration["email"])
        self.input_password(auth_credentials.registration["password"])
        self.click_login_button()
