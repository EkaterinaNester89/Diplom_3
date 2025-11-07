import allure

from locators.home_page import HomePageLocators
from .base_page import BasePage


class HomePage(BasePage):
    @allure.step("Нажимаем по кнопке Конструктор")
    def click_constructor_button(self):
        self.click_to_element(HomePageLocators.CONSTRUCTOR_BUTTON)