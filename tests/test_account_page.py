import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from data import URLs


# TODO do smth with fixture, and login.submit_login_form
class TestAccountPage:
    def test_personal_account(self, driver, create_and_login_user_via_API): 
        login = LoginPage(driver)
        account = AccountPage(driver)

        login.submit_login_form()
        account.click_account_button()
        account.wait_until_page_loaded()
        actual_url = account.get_current_page()
        expected_url = URLs.personal_account_page

        assert actual_url == expected_url

    def test_order_history(self,driver, create_and_login_user_via_API):
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

    def test_user_logout(self,driver, create_and_login_user_via_API):
        login = LoginPage(driver)
        account = AccountPage(driver)

        login.submit_login_form()
        account.click_account_button()
        account.wait_until_page_loaded()
        account.click_logout_button()

        actual_url = account.get_current_page()
        
        expected_url = URLs.login_page

        assert actual_url == expected_url
    