import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage():

    PERSONAL_ACCOUNT = [By. XPATH, './/p[text() = "Личный Кабинет"]']
    LOGIN_ACCOUNT_BUTTON = [By. XPATH, './/button[text() = "Войти в аккаунт"]']
    CONSTRUCTOR_BUTTON = [By. XPATH, './/p[text() = "Конструктор"]']
    CONSTRUCTOR_SECTION = [By. XPATH, './/h1[text() ="Соберите бургер"]']
    ORDER_FEED = [By. XPATH, './/p[text() = "Лента Заказов"]']
    ORDER_FEED_TITLE = [By. XPATH, './/h1[text() ="Лента заказов"]']
    ORDER_LIST_SECTION = [By. XPATH,
                          './/span[@class = "constructor-element__row"]']
    INGREDIENT_BUN = [By. XPATH, './/p[text() = "Флюоресцентная булка R2-D3"]']
    INGREDIENT_DETAILS_POPUP = [
        By. XPATH, './/h2[text() ="Детали ингредиента"]/ancestor::section[contains(@class, "Modal_modal")]']
    CLOSE_BUTTON = [
        By. XPATH, './/button[contains(@class, "Modal_modal__close_modified__")]']
    INGREDIENT_COUNTER = [
        By. XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]/div/p[contains(@class, "counter_counter__num__")]']
    INGREDIENT_SAUCE = [By. XPATH,
                        './/p[text() ="Соус фирменный Space Sauce"]']
    SUBMIT_ORDER = [By. XPATH, './/button[text() = "Оформить заказ"]']
    CONFIRMATION_POPUP = [By. XPATH,
                          './/p[text() ="Ваш заказ начали готовить"]']
    CONFIRMATION_POPUP_LOADING = [
        By.XPATH, "//div[contains(@class, 'Modal_modal__loading')]"]
    CONFIRMATION_POPUP_ORDER_ID = [
        By. XPATH, './/section[contains(@class, "Modal_modal_opened")]//h2[contains(@class, "Modal_modal__title")]']
    CLOSE_CONFIRMATION__POPUP = [
        By. XPATH, './/section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "Modal_modal__close_modified")]']


    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)


    def find_element(self, element):
        return self.driver.find_element(*element)

    def wait_until_clickable(self, element, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.element_to_be_clickable(element))

    def wait_until_visible(self, element, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((element)))

    def wait_until_not_visible(self, element, time=10):
        WebDriverWait(self.driver, time).until_not(
            expected_conditions.visibility_of_element_located((element)))

    def wait_until_presence(self, element, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located((element)))

    def wait_until_not_presence(self, element, time=10):
        WebDriverWait(self.driver, time).until_not(
            expected_conditions.presence_of_element_located((element)))

    def wait_until_text_not(self, element, text, time=10):
        WebDriverWait(self.driver, time).until_not(
            expected_conditions.text_to_be_present_in_element(element, text))

    @allure.step('Проверь URL')
    def get_current_page(self):
        return self.driver.current_url

    @allure.step('Нажми на "Личный аккаунт"')
    def click_account_button(self):
        self.find_element(self.PERSONAL_ACCOUNT).click()

    @allure.step('Нажми на "Войти в аккаунт"')
    def click_login_account_button(self):
        self.wait_until_clickable(self.LOGIN_ACCOUNT_BUTTON, time=10)
        self.find_element(self.LOGIN_ACCOUNT_BUTTON).click()

    @allure.step('Нажми на "Лента заказов"')
    def click_orders_feed(self):
        self.find_element(self.ORDER_FEED).click()

    @allure.step('Проверь что секция "Лента заказов" представлена на странице')
    def get_orders_feed(self):
        self.wait_until_presence(self.ORDER_FEED_TITLE)
        return self.find_element(self.ORDER_FEED_TITLE)

    @allure.step('Нажми на "Конструктор"')
    def click_constructor_button(self):
        self.find_element(self.CONSTRUCTOR_BUTTON).click()

    @allure.step('Проверь что секция "Собери бургер" представлена на странице')
    def get_constructor(self):
        self.wait_until_presence(self.CONSTRUCTOR_SECTION)
        return self.find_element(self.CONSTRUCTOR_SECTION)

    @allure.step('Кликни на ингридиент')
    def click_ingredient(self):
        self.find_element(self.INGREDIENT_BUN).click()

    @allure.step('Проверь что появилось окошко с деталями')
    def is_details_popup_visible(self):
        self.wait_until_visible(self.INGREDIENT_DETAILS_POPUP)
        details_popup = self.find_element(self.INGREDIENT_DETAILS_POPUP)
        return details_popup.value_of_css_property('visibility') == 'visible'

    @allure.step('Проверь что скрылось окошко с деталями')
    def is_details_popup_hidden(self):
        self.wait_until_not_visible(self.INGREDIENT_DETAILS_POPUP)
        details_popup = self.find_element(self.INGREDIENT_DETAILS_POPUP)
        return details_popup.value_of_css_property('visibility') == 'hidden'

    @allure.step('Закрой окошко с деталями')
    def click_close_button(self):
        self.find_element(self.CLOSE_BUTTON).click()
        self.wait_until_presence(self.CONSTRUCTOR_SECTION)

    @allure.step('Перетащи ингридиент в Заказ')
    def drag_and_drop_ingredient(self):
        draggable = self.find_element(self.INGREDIENT_SAUCE)
        droppable = self.find_element(self.ORDER_LIST_SECTION)

        self.actions.drag_and_drop(draggable, droppable).perform()

    @allure.step('Перетащи булочку в Заказ')
    def drag_and_drop_bun(self):
        self.wait_until_clickable(self.INGREDIENT_BUN)
        draggable = self.find_element(self.INGREDIENT_BUN)
        droppable = self.find_element(self.ORDER_LIST_SECTION)

        self.actions.drag_and_drop(draggable, droppable).perform()

    @allure.step('Проверь кроличество ингридиентов')
    def get_ingredients_count(self):
        return self.find_element(self.INGREDIENT_COUNTER).text

    @allure.step('Кликни на "Оформить заказ"')
    def click_submit_order(self):
        self.find_element(self.SUBMIT_ORDER).click()

    @allure.step('Проверь, что заказ создался')
    def get_confirmation_popup(self):
        return self.find_element(self.CONFIRMATION_POPUP)

    @allure.step('Закрой окно с деталями заказа')
    def close_confirmation_popup(self):
        self.wait_until_not_visible(self.CONFIRMATION_POPUP_LOADING, 50)
        self.wait_until_text_not(self.CONFIRMATION_POPUP_ORDER_ID, '9999', 500)
        self.find_element(self.CLOSE_CONFIRMATION__POPUP).click()

    @allure.step('Проверь id заказа')
    def get_order_id_from_confirmation_popup(self):
        self.wait_until_not_visible(self.CONFIRMATION_POPUP_LOADING, 50)
        self.wait_until_text_not(self.CONFIRMATION_POPUP_ORDER_ID, '9999')
        return self.find_element(self.CONFIRMATION_POPUP_ORDER_ID).text

    
