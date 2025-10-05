from pages.orders_feed_page import OrdersFeed
from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TestOrdersFeed:

    def test_order_details_popup(self, driver):
        order = OrdersFeed(driver)

        order.click_orders_feed()
        order.click_last_order()
        order_popup = order.get_order_details_popup()

        assert order_popup.is_displayed()

    def test_users_order_is_displayed_in_orders_feed(self, driver, create_and_login_user_via_API):
        order = OrdersFeed(driver)
        login = LoginPage(driver)
        account = AccountPage(driver)

        login.submit_login_form()
        order.drag_and_drop_bun()
        order.drag_and_drop_ingredient()
        order.click_submit_order()
        order.close_confirmation_popup()
        order.click_account_button()
        account.wait_until_page_loaded()
        account.click_orders_history()
        order_id = account.get_user_last_order_id()
        order.click_orders_feed()
        user_order_in_feed = order.get_user_order_by_id(order_id)

        assert user_order_in_feed.is_displayed()
