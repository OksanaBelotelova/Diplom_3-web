import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    ACCOUNT_BUTTON = [By. XPATH, './/p[text() = "Личный Кабинет"]']
    LOGIN_ACCOUNT_BUTTON = [By. XPATH, './/button[text() = "Войти в аккаунт"]']

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element):
        return self.driver.find_element(*element)
    
    def wait_until_clickable(self,element, time = 10 ):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(element))

    def wait_until_visible(self,element, time = 10):
        WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located((element)))
    
    @allure.step('Check URL')
    def get_current_page(self):
        return self.driver.current_url

    @allure.step('Press on "Личный аккаунт"')
    def click_account_button(self):
        self.find_element(self.ACCOUNT_BUTTON).click()

    @allure.step('Press on "Войти в аккаунт"')
    def click_login_account_button(self):
        self.wait_until_clickable(self.LOGIN_ACCOUNT_BUTTON, time = 10)
        self.find_element(self.LOGIN_ACCOUNT_BUTTON).click()
        

    

