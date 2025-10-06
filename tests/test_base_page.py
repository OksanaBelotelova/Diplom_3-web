import allure
from pages.login_page import LoginPage
from pages.base_page import BasePage
from data import URLs


class TestBasePage:

    def test_orders_feed(self, driver):
        base = BasePage(driver)
        base.click_orders_feed()
        orders = base.get_orders_feed()

        assert orders.is_displayed()

    def test_constructor(self, driver):
        base = BasePage(driver)
        base.click_orders_feed()
        base.click_constructor_button()
        constructor_section = base.get_constructor()

        assert constructor_section.is_displayed()

    def test_ingredient_details(self, driver):
        base = BasePage(driver)
        base.click_ingredient()
        details_popup = base.get_details_popup()

        assert details_popup.is_displayed()

    def test_close_ingredient_details(self, driver):
        base = BasePage(driver)
        base.click_ingredient()

        assert base.is_details_popup_visible()

        base.click_close_button()

        assert base.is_details_popup_hidden()

    def test_count_of_ingredients(self, driver):
        base = BasePage(driver)
        base.drag_and_drop_ingredient()
        count = base.get_ingredients_count()

        assert count == '1'

    # TODO do one step "create_order" instead drag_and_drop and submit_order
    def test_confirmation_order(self, driver, create_and_login_user_via_API):
        login = LoginPage(driver)
        base = BasePage(driver)

        login.submit_login_form()
        base.drag_and_drop_bun()
        base.drag_and_drop_ingredient()
        base.click_submit_order()
        submit_message = base.get_confirmation_popup()

        assert submit_message.is_displayed()
