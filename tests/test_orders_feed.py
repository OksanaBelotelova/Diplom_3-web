import allure
from pages.orders_feed_page import OrdersFeed
from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TestOrdersFeed:

    @allure.title('Появление всплывающего окна с деталями заказа')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями заказа')
    def test_order_details_popup(self, driver):
        order = OrdersFeed(driver)

        order.click_orders_feed()
        order.click_last_order()
        order_popup = order.get_order_details_popup()

        assert order_popup.is_displayed()


    @allure.title('Заказы пользователя отображаются в Ленте заказов')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_is_displayed_in_orders_feed(self, driver):
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


    @allure.title('Работа счетчика "Выполнено за всё время"')
    @allure.description('При создании нового заказа счётчик "Выполнено за всё время" увеличивается,')
    def test_all_orders_counter(self, driver):
        order = OrdersFeed(driver)
        login = LoginPage(driver)

        login.submit_login_form()
        order.click_orders_feed()
        all_orders_number_before = order.get_all_orders_number()
        order.click_constructor_button()
        order.drag_and_drop_bun()
        order.drag_and_drop_ingredient()
        order.click_submit_order()
        order.close_confirmation_popup()
        order.click_orders_feed()
        all_orders_number_after = order.get_all_orders_number()

        assert all_orders_number_before < all_orders_number_after


    @allure.title('Работа счетчика "Выполнено за сегодня')
    @allure.description('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_todays_orders_counter(self, driver):
        order = OrdersFeed(driver)
        login = LoginPage(driver)

        login.submit_login_form()
        order.click_orders_feed()
        todays_orders_number_before = order.get_todays_orders_number()
        order.click_constructor_button()
        order.drag_and_drop_bun()
        order.drag_and_drop_ingredient()
        order.click_submit_order()
        order.close_confirmation_popup()
        order.click_orders_feed()
        todays_orders_number_after = order.get_todays_orders_number()

        assert todays_orders_number_before < todays_orders_number_after


    @allure.title('Появление заказа в разделе "В работе"')
    @allure.description('После оформления заказа его номер появляется в разделе "В работе"')
    def test_new_order_comes_to_in_progress_list(self, driver):

        order = OrdersFeed(driver)
        login = LoginPage(driver)

        login.submit_login_form()
        order.drag_and_drop_bun()
        order.drag_and_drop_ingredient()
        order.click_submit_order()
        order_id = order.get_order_id_from_confirmation_popup()
        order.close_confirmation_popup()
        order.click_orders_feed()
        order_in_progress = order.get_order_in_progress_by_id(order_id)

        assert order_in_progress.is_displayed()
