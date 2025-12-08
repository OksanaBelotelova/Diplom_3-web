import allure
from pages.login_page import LoginPage
from data import URLs, AuthCredentials


class TestLoginPage:

    @allure.title("Проверь кнопу 'Восстановить пароль'")
    @allure.description("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'",)
    def test_restore_password_button(self, driver):
        login = LoginPage(driver)
        
        login.click_login_account_button()
        login.click_restore_password_button()
        
        expected_url = URLs.reset_password_page
        actual_url = login.get_current_page()

        assert actual_url == expected_url


    @allure.title("Проверь кнопу 'Восстановить'")
    @allure.description("Ввод почты и клик по кнопке «Восстановить» переводит на страницу восстановления пароля и ввода кода из письма")
    def test_restore_button(self, driver):
        login = LoginPage(driver)
        
        login.click_login_account_button()
        login.click_restore_password_button()
        login.input_email(AuthCredentials.registration['email'])
        login.click_restore_button()
        
        expected_url = URLs.restore_password_page
        actual_url = login.get_current_page()
        
        assert actual_url == expected_url


    @allure.title("Проверь кнопу 'Показать/скрыть пароль'")
    @allure.description("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_show_hide_password_button(self, driver):
        login = LoginPage(driver)
        
        login.click_login_account_button()
        login.click_restore_password_button()
        login.input_email(AuthCredentials.registration['email'])
        login.click_restore_button()
        login.click_show_password_button()
        
        active_new_password_field_wrapper = login.get_active_new_password_field_wrapper()

        assert active_new_password_field_wrapper.is_displayed()
