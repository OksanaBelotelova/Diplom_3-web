from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL_FIELD = [By. XPATH, './/input[@name = "name"]']
    PASSWORD_FIELD = [By. XPATH, './/input[@name = "Пароль"]']
    LOGIN_BUTTON = [By. XPATH, './/button[text() = "Войти"]']
    RESTORE_PASSWORD_BUTTON = [By. XPATH, './/a[@href = "/forgot-password"]']
    RESTORE_BUTTON = [By. XPATH, './/button[text() = "Восстановить"]']
    SHOW_HIDE_BUTTON = [By. XPATH, './/div[@class="input__icon input__icon-action"]/svg']
    

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Press on "Восстановить пароль"')
    def click_restore_password_button(self):
        self.find_element(self.RESTORE_PASSWORD_BUTTON).click()

    @allure.step('Input your email')
    def input_email(self,email):
        self.find_element(self.EMAIL_FIELD).send_keys(email)
    
    @allure.step('Press on "Восстановить"')
    def click_restore_button(self):
        self.wait_until_clickable(self.RESTORE_BUTTON, time = 10)
        self.find_element(self.RESTORE_BUTTON).click()

    @allure.step('Press on show password button')
    def click_show_password_button(self):
        self.find_element(self.SHOW_HIDE_BUTTON).click()

    