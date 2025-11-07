import allure

from locators.home_page import HomePageLocators
from .base_page import BasePage


class HomePage(BasePage):
    @allure.step("Нажимаем по кнопке Конструктор")
    def click_constructor_button(self):
        self.click_to_element(HomePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажимаем по кнопке Лента заказов")
    def click_feed_button(self):
        self.click_to_element(HomePageLocators.FEED_BUTTON)

    @allure.step("Нажимаем по ингредиенту")
    def click_ingredient(self):
        self.click_to_element(HomePageLocators.INGREDIENT)
        return True

    @allure.step("Ищем модальное окно детали ингредиента")
    def check_modal_ingredients_details(self):
        return self.find_element(HomePageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Нажимаем по закрытию модального окна ингредиента")
    def click_ingredient_details_modal_close_button(self):
        self.click_to_element(HomePageLocators.INGREDIENT_DETAILS_MODAL_CLOSE_BUTTON)
        return True

    @allure.step("Получаем стоимость ингредиентов в будущем заказе")
    def get_price_ingredients_future_order(self):
        return int(self.get_text(HomePageLocators.ORDER_BASKET_TOTAL_COUNT))