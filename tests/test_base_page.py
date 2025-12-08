import allure
from pages.login_page import LoginPage
from pages.base_page import BasePage



class TestBasePage:

    @allure.title('Переход по клику на "Лента заказов"')
    @allure.description('Кликая на кнопку "Лента заказов" пользователь переходит в раздел "Лента заказов"')
    def test_orders_feed(self, driver):
        base = BasePage(driver)
        
        base.click_orders_feed()
        orders = base.get_orders_feed()

        assert orders.is_displayed()


    @allure.title('Переход по клику на "Конструктор"')
    @allure.description('Кликая на кнопку "Конструктор" пользователь переходит в раздел "Соберите бургер"')
    def test_constructor(self, driver):
        base = BasePage(driver)
        
        base.click_orders_feed()
        base.click_constructor_button()
        constructor_section = base.get_constructor()

        assert constructor_section.is_displayed()


    @allure.title('Появление всплывающего окна с деталями ингридиента')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями ингридиента')
    def test_ingredient_details(self, driver):
        base = BasePage(driver)
        
        base.click_ingredient()
        base.is_details_popup_visible()
        
        assert base.is_details_popup_visible()


    @allure.title('Закрытие всплывающего окна с деталями ингридиента')
    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details(self, driver):
        base = BasePage(driver)
        
        base.click_ingredient()
        base.is_details_popup_visible()
        base.click_close_button()

        assert base.is_details_popup_hidden()


    @allure.title('Увеличение счетчика ингридиента')
    @allure.description('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_count_of_ingredients(self, driver):
        base = BasePage(driver)
        
        base.drag_and_drop_ingredient()
        count = base.get_ingredients_count()

        assert count == '1'


    @allure.title('Оформление заказа для залогиненного пользователя')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_confirmation_order(self, driver):
        login = LoginPage(driver)
        base = BasePage(driver)

        login.submit_login_form()
        base.drag_and_drop_bun()
        base.drag_and_drop_ingredient()
        base.click_submit_order()
        submit_message = base.get_confirmation_popup()

        assert submit_message.is_displayed()
