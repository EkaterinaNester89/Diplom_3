import allure
from locators.order_page import OrderPageLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title(
        "Проверка при создании нового заказа счётчик «Выполнено за всё время» увеличивается"
    )
    def test_new_order_increment_completed_all_time_count_success(self, driver):
        login_page = LoginPage(driver)
        login_page.get_driver_signed_in()

        with allure.step(
            "Идем на страницу заказов и получаем значение счетчика «Выполнено за всё время»"
        ):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            all_orders_count_initially = order_page.get_quantity_order_all_time()

        home_page = HomePage(driver)
        home_page.make_order()

        with allure.step(
            "Идем на страницу заказов и получаем значение счетчика «Выполнено за всё время»"
        ):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            all_orders_count_finish = order_page.get_quantity_order_all_time()
        assert all_orders_count_finish > all_orders_count_initially

    @allure.title(
        "Проверка при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;"
    )
    def test_new_order_increment_completed_today_count_success(self, driver):
        login_page = LoginPage(driver)
        login_page.get_driver_signed_in()
        with allure.step(
            "Идем на страницу заказов и получаем значение счетчика «Выполнено за сегодня» "
        ):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            today_orders_count_initially = order_page.get_quantity_order_today()

        home_page = HomePage(driver)
        home_page.make_order()

        with allure.step(
            "Идем на страницу заказов и получаем значение счетчика «Выполнено за сегодня» "
        ):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            today_orders_count_finish = order_page.get_quantity_order_today()
        assert today_orders_count_finish > today_orders_count_initially

    @allure.title(
        "Проверка после оформления заказа его номер появляется в разделе «В работе»."
    )
    def test_new_order_number_is_work_in_progress_success(self, driver):
        login_page = LoginPage(driver)
        login_page.get_driver_signed_in()

        home_page = HomePage(driver)
        home_page.make_order()

        order_number = home_page.get_order_number()

        with allure.step(
            "Идем на страницу заказов и получаем значение заказов в работе"
        ):
            order_page = OrderPage(driver)
            order_page.open_feed_page()
            method, locator = OrderPageLocators.ORDERS_IN_PROGRESS
            locator = locator.format(order_number)
            assert order_page.find_element((method, locator))
