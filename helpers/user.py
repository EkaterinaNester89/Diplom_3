import allure
import requests

from data.user import UserAPIData
from .common import CommonApiHelper


class UserAPIHelper(CommonApiHelper):
    @allure.step("Отправка запроса для регистрирования пользователя в системе")
    def send_request_create(self, data):
        return requests.request(
            url=UserAPIData.USER_CREATE_URL[0],
            method=UserAPIData.USER_CREATE_URL[1],
            json=data,
        )

    @allure.step("Создание тестовых данных пользователя")
    def generate_user_create_data(self, keys=None):
        name = self.generate_random_string(23)
        password = self.generate_random_string(23)
        email = f"{self.generate_random_string(15)}@{self.generate_random_string(15)}notexists.com"

        full_data = {"name": name, "password": password, "email": email}

        if keys is None:
            return full_data

        return {k: full_data[k] for k in keys if k in full_data}

    @allure.step("Получение данных нового тестового пользователя")
    def data_random_new_user_account(self, keys=None):
        user_data = self.generate_user_create_data(keys=keys)
        response = self.send_request_create(user_data)
        if response.status_code == 200:
            return user_data
