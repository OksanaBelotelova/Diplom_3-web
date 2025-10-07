import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from data import URLs


class TestAccountPage:

    @allure.title('Переход по клику на "Личный кабинет"')
    @allure.description('Переход на страницу личного кабинета по кнопке "Личный кабинет"')
    def test_personal_account(self, driver):
        login = LoginPage(driver)
        account = AccountPage(driver)

        login.submit_login_form()
        account.click_account_button()
        account.wait_until_page_loaded()
        actual_url = account.get_current_page()
        expected_url = URLs.personal_account_page

        assert actual_url == expected_url


    @allure.title('Переход в раздел "История заказов"')
    @allure.description('Переход в раздел истории заказов по кнопке "История заказов"')
    def test_order_history(self, driver):
        login = LoginPage(driver)
        account = AccountPage(driver)

        login.submit_login_form()
        account.click_account_button()
        account.wait_until_page_loaded()
        account.click_orders_history()
        account.wait_until_page_loaded()

        actual_url = account.get_current_page()
        expected_url = URLs.order_history_page

        assert actual_url == expected_url


    @allure.title('Выход из аккаунта')
    @allure.description('Кликая на кнопку "Выход" юзер попадает на страницу регистрации')
    def test_user_logout(self, driver):
        login = LoginPage(driver)
        account = AccountPage(driver)

        login.submit_login_form()
        account.click_account_button()
        account.wait_until_page_loaded()
        account.click_logout_button()

        actual_url = account.get_current_page()
        expected_url = URLs.login_page

        assert actual_url == expected_url
