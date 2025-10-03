import allure
from pages.login_page import LoginPage
from data import URLs
class TestLoginPage:
   
    @allure.title("Проверь кнопу 'Восстановить пароль'")
    @allure.description("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'",)
    def test_restore_password_button(self, driver):
        login = LoginPage(driver)
        login.click_login_account_button()
        login.click_restore_password_button()
        expected_url = URLs.reset_password_page
        assert login.get_current_page() == expected_url

    