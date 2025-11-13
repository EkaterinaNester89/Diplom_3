import allure

from data.common import URLS
from locators.order_page import OrderPageLocators
from .base_page import BasePage


class OrderPage(BasePage):
    @allure.step(f"Открываем страницу {URLS.FEED_PAGE}")
    def open_feed_page(self):
        self.open_url(URLS.FEED_PAGE)

    @allure.step("Получаем количество заказов за все время")
    def get_quantity_order_all_time(self):
        return int(self.get_text(OrderPageLocators.COUNTER_DONE_ALL_TIME))

    @allure.step("Получаем количество заказов за сегодня")
    def get_quantity_order_today(self):
        return int(self.get_text(OrderPageLocators.COUNTER_DONE_TODAY))
