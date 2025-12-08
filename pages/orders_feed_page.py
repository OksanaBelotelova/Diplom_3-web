from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class OrdersFeed(BasePage):

    ORDERS_FEED_LOADING = [By.XPATH, '//div[text() = "Загрузка..."]']
    ORDER_ID = [
        By.XPATH, './/div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, "text_type_digits-default")][contains(text(), "{0}")]']
    LAST_ORDER_LINK = [
        By.XPATH, './/a[contains(@class, "OrderHistory_link")][1]']
    ORDER_DETAILS_POPUP = [
        By.XPATH, './/section[contains(@class, "Modal_modal_opened")]']
    ALL_ORDERS_COUNTER = [
        By.XPATH, './/div[contains(@class, "OrderFeed_ordersData")]/div[contains(@class,"undefined")]/p[contains(@class, "OrderFeed_number")]']
    TODAYS_ORDER_COUNTER = [
        By.XPATH, './/div[contains(@class, "OrderFeed_ordersData")]/div[2]/p[contains(@class, "OrderFeed_number")]']
    ORDER_ID_IN_PROGRESS = [
        By.XPATH, './/ul[contains(@class, "OrderFeed_orderListReady")]//text()[contains(.,"{0}")]/parent::li']

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Нажми на заказ')
    def click_last_order(self):
        self.wait_until_clickable(self.LAST_ORDER_LINK)
        self.find_element(self.LAST_ORDER_LINK).click()

    @allure.step('Проверь, что появилось окно с деталями заказа')
    def get_order_details_popup(self):
        return self.find_element(self.ORDER_DETAILS_POPUP)

    @allure.step('Проверь, что заказ с нужным id представлен в "Ленте заказов"')
    def get_user_order_by_id(self, order_id):
        self.wait_until_not_presence(self.ORDERS_FEED_LOADING)
        formatted_xpath = [self.ORDER_ID[0], self.ORDER_ID[1].format(order_id)]
        return self.find_element(formatted_xpath)

    @allure.step('Проверь, что заказ с нужным id представлян в разделе "В работе"')
    def get_order_in_progress_by_id(self, order_id):
        self.wait_until_presence(self.ORDERS_FEED_LOADING)
        formatted_xpath = [self.ORDER_ID_IN_PROGRESS[0],
                           self.ORDER_ID_IN_PROGRESS[1].format(order_id)]
        self.wait_until_presence(formatted_xpath, 50)
        return self.find_element(formatted_xpath)

    @allure.step('Проверь количество заказов за все время')
    def get_all_orders_number(self):
        self.wait_until_not_presence(self.ORDERS_FEED_LOADING)
        return int(self.find_element(self.ALL_ORDERS_COUNTER).text)

    @allure.step('Проверь количество заказов за сегодня')
    def get_todays_orders_number(self):
        self.wait_until_not_presence(self.ORDERS_FEED_LOADING)
        return int(self.find_element(self.TODAYS_ORDER_COUNTER).text)
