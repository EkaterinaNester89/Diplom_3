import allure

from data.common import URLS
from locators.home_page import HomePageLocators
from pages.home_page import HomePage


class TestHomePage:

    @allure.title("Проверка переход по клику на «Конструктор»")
    def test_redirect_click_constructor_success(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_constructor_button()
        assert URLS.HOME_PAGE == home_page.get_current_url()

    @allure.title("Проверка переход по клику на раздел «Лента заказов»")
    def test_redirect_click_feed_success(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_feed_button()
        assert URLS.FEED_PAGE == home_page.get_current_url()

    @allure.title(
        "Проверка кликнуть на ингредиент, появится всплывающее окно с деталями"
    )
    def test_click_ingredient_shows_modal_success(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_ingredient()
        assert home_page.check_modal_ingredients_details()

    @allure.title("Проверка всплывающее окно закрывается кликом по крестику")
    def test_click_close_icon_close_modal_success(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_ingredient()
        assert home_page.click_ingredient_details_modal_close_button()

    @allure.title(
        "Проверка при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается."
    )
    def test_click_add_ingredient_increment_count_success(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        initial_value = home_page.get_price_ingredients_future_order()
        source_element = home_page.find_element(HomePageLocators.INGREDIENT)
        destination_element = home_page.find_element(HomePageLocators.ORDER_BASKET)
        home_page.drag_and_drop(source_element, destination_element)
        finish_value = home_page.get_price_ingredients_future_order()
        assert initial_value < finish_value
