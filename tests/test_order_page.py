import allure


class TestOrderPage:

    @allure.title("Проверка при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_new_order_increment_completed_count_success(self):
        pass
    @allure.title("Проверка при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;")
    def test_new_order_increment_completed_today_count_success(self):
        pass
    @allure.title("Проверка после оформления заказа его номер появляется в разделе «В работе».")
    def test_new_order_number_is_work_in_progress_success(self):
        pass
