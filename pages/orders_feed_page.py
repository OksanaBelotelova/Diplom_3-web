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

    def __init__(self, driver):
        super().__init__(driver)

    def click_last_order(self):
        self.wait_until_clickable(self.LAST_ORDER_LINK)
        self.find_element(self.LAST_ORDER_LINK).click()

    def get_order_details_popup(self):
        return self.find_element(self.ORDER_DETAILS_POPUP)

    def get_user_order_by_id(self, order_id):
        self.wait_until_not_presence(self.ORDERS_FEED_LOADING)
        formatted_xpath = [self.ORDER_ID[0], self.ORDER_ID[1].format(order_id)]
        return self.find_element(formatted_xpath)
