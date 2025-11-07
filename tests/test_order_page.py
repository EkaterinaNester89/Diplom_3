import time

import allure
from selenium.webdriver.support.wait import WebDriverWait

from helpers.user import UserAPIHelper
from locators.home_page import HomePageLocators
from locators.login_page import LoginPageLocators
from locators.order_page import OrderPageLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Проверка при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_new_order_increment_completed_all_time_count_success(self, driver):
        with allure.step('Создаем нового пользователя'):
            user_api = UserAPIHelper()
            user_data = user_api.data_random_new_user_account()
        with allure.step('Идем на страницу заказов и получаем значение счетчика «Выполнено за всё время»'):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            all_orders_count_initially = order_page.get_quantity_order_all_time()
        with allure.step('Логинимся под пользователем'):
            login_page = LoginPage(driver)
            login_page.open_login_page()
            email = user_data.get('email')
            password = user_data.get('password')
            login_page.set_email(email)
            login_page.set_password(password)
            time.sleep(2)
            login_page.click_to_element(LoginPageLocators.ENTER_BUTTON)
            time.sleep(2)
        with allure.step('Идем на главную и делаем заказ'):
            home_page = HomePage(driver)
            home_page.open_home_page()
            source_element = home_page.find_element(HomePageLocators.INGREDIENT)
            destination_element = home_page.find_element(HomePageLocators.ORDER_BASKET)
            home_page.drag_and_drop(source_element, destination_element)
            time.sleep(2)
            home_page.click_to_element(HomePageLocators.ORDER_MAKE_BUTTON)
            time.sleep(2)
            home_page.wait_element_to_be_clickable(HomePageLocators.ORDER_NUMBER_DONE)
        with allure.step('Идем на страницу заказов и получаем значение счетчика «Выполнено за всё время»'):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            all_orders_count_finish = order_page.get_quantity_order_all_time()
        assert all_orders_count_finish > all_orders_count_initially

    @allure.title("Проверка при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;")
    def test_new_order_increment_completed_today_count_success(self,driver):
        with allure.step('Создаем нового пользователя'):
            user_api = UserAPIHelper()
            user_data = user_api.data_random_new_user_account()
        with allure.step('Идем на страницу заказов и получаем значение счетчика «Выполнено за сегодня» '):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            today_orders_count_initially = order_page.get_quantity_order_today()
        with allure.step('Логинимся под пользователем'):
            login_page = LoginPage(driver)
            login_page.open_login_page()
            email = user_data.get('email')
            password = user_data.get('password')
            login_page.set_email(email)
            login_page.set_password(password)
            time.sleep(2)
            login_page.click_to_element(LoginPageLocators.ENTER_BUTTON)
            time.sleep(2)
        with allure.step('Идем на главную и делаем заказ'):
            home_page = HomePage(driver)
            home_page.open_home_page()
            source_element = home_page.find_element(HomePageLocators.INGREDIENT)
            destination_element = home_page.find_element(HomePageLocators.ORDER_BASKET)
            home_page.drag_and_drop(source_element, destination_element)
            time.sleep(2)
            home_page.click_to_element(HomePageLocators.ORDER_MAKE_BUTTON)
            time.sleep(2)
            home_page.wait_element_to_be_clickable(HomePageLocators.ORDER_NUMBER_DONE)
        with allure.step('Идем на страницу заказов и получаем значение счетчика «Выполнено за сегодня» '):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            today_orders_count_finish = order_page.get_quantity_order_today()
        assert today_orders_count_finish > today_orders_count_initially

    @allure.title("Проверка после оформления заказа его номер появляется в разделе «В работе».")
    def test_new_order_number_is_work_in_progress_success(self,driver):
        with allure.step('Создаем нового пользователя'):
            user_api = UserAPIHelper()
            user_data = user_api.data_random_new_user_account()
        with allure.step('Логинимся под пользователем'):
            login_page = LoginPage(driver)
            login_page.open_login_page()
            email = user_data.get('email')
            password = user_data.get('password')
            login_page.set_email(email)
            login_page.set_password(password)
            time.sleep(2)
            login_page.click_to_element(LoginPageLocators.ENTER_BUTTON)
            time.sleep(2)
        with allure.step('Идем на главную и делаем заказ'):
            home_page = HomePage(driver)
            home_page.open_home_page()
            source_element = home_page.find_element(HomePageLocators.INGREDIENT)
            destination_element = home_page.find_element(HomePageLocators.ORDER_BASKET)
            home_page.drag_and_drop(source_element, destination_element)
            time.sleep(2)
            home_page.click_to_element(HomePageLocators.ORDER_MAKE_BUTTON)
            time.sleep(2)
        with allure.step('Получаем номер заказа'):
            home_page.wait_element_to_be_clickable(HomePageLocators.ORDER_NUMBER_DONE)
            WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element(*HomePageLocators.ORDER_NUMBER_DONE).text != str('9999')
            )
            number_order = home_page.get_text(HomePageLocators.ORDER_NUMBER_DONE)
        with allure.step('Идем на страницу заказов и получаем значение заказов в работе'):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            method, locator = OrderPageLocators.ORDERS_IN_PROGRESS
            locator = locator.format(number_order)
            assert order_page.find_element((method, locator))
