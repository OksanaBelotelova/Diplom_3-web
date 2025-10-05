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
    NEW_PASSWORD_FIELD = [By. XPATH, './/div[@class="input__container"]']
    NEW_PASSWORD_FIELD_WRAPPER = [By. XPATH,
                                  './/div[@class="input__container"]/div']

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Press on "Восстановить пароль"')
    def click_restore_password_button(self):
        self.find_element(self.RESTORE_PASSWORD_BUTTON).click()

    @allure.step('Input your email')
    def input_email(self, email):
        self.find_element(self.EMAIL_FIELD).send_keys(email)

    @allure.step('Press on "Восстановить"')
    def click_restore_button(self):
        self.wait_until_clickable(self.RESTORE_BUTTON, time=10)
        self.find_element(self.RESTORE_BUTTON).click()
        self.wait_until_clickable(self.SHOW_HIDE_BUTTON, time=10)

    @allure.step('Press on show password button')
    def click_show_password_button(self):
        self.find_element(self.SHOW_HIDE_BUTTON).click()

    def get_border_color(self):
        return self.NEW_PASSWORD_FIELD_WRAPPER.value_of_css_property('border')

    def input_password(self, password):
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def submit_login_form(self):
        auth_credentials = AuthCredentials()
        self.click_login_account_button()
        self.input_email(auth_credentials.registration["email"])
        self.input_password(auth_credentials.registration["password"])
        self.click_login_button()

    