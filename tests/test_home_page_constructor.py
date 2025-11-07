import allure

from data.common import URLS
from pages.home_page import HomePage


class TestHomePage:

    @allure.title("Проверка переход по клику на «Конструктор»")
    def test_redirect_click_constructor_success(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_constructor_button()
        assert URLS.HOME_PAGE == home_page.get_current_url()

    @allure.title("Проверка кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient_shows_modal_success(self):
        pass

    @allure.title("Проверка всплывающее окно закрывается кликом по крестику")
    def test_click_close_icon_close_modal_success(self):
        pass

    @allure.title("Проверка при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.")
    def test_click_add_ingredient_increment_count_success(self):
        pass
