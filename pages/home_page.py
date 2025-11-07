import time

import allure
from selenium.webdriver.support.wait import WebDriverWait

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

    @allure.step("Делаем заказ на главной странице")
    def make_order(self):
        self.open_home_page()
        source_element = self.find_element(HomePageLocators.INGREDIENT)
        destination_element = self.find_element(HomePageLocators.ORDER_BASKET)
        self.drag_and_drop(source_element, destination_element)
        time.sleep(2)
        self.click_to_element(HomePageLocators.ORDER_MAKE_BUTTON)
        time.sleep(2)
        self.wait_element_to_be_clickable(HomePageLocators.ORDER_NUMBER_DONE)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        self.wait_element_to_be_clickable(HomePageLocators.ORDER_NUMBER_DONE)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*HomePageLocators.ORDER_NUMBER_DONE).text
            != str("9999")
        )
        return self.get_text(HomePageLocators.ORDER_NUMBER_DONE)
