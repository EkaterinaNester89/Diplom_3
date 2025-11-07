import time

import allure

from data.common import URLS
from helpers.user import UserAPIHelper
from locators.login_page import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Заполняем "емайл"')
    def set_email(self, email):
        self.set_text(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Заполняем "Пароль"')
    def set_password(self, password):
        self.set_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step(f"Заходим страницу {URLS.LOGIN_PAGE}")
    def open_login_page(self):
        self.open_url(URLS.LOGIN_PAGE)

    @allure.step("Логинимся под пользователем")
    def do_login(self, user_data):
        self.open_login_page()
        email = user_data.get("email")
        password = user_data.get("password")
        self.set_email(email)
        self.set_password(password)
        time.sleep(2)
        self.click_to_element(LoginPageLocators.ENTER_BUTTON)
        time.sleep(2)

    @allure.step("Создаем нового пользователя")
    def create_new_user(self):
        user_api = UserAPIHelper()
        return user_api.data_random_new_user_account()

    @allure.step("Логиним драйвер")
    def get_driver_signed_in(self):
        data = self.create_new_user()
        self.do_login(data)
