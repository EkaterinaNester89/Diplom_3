import allure

from locators.login_page import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Заполняем "емайл"')
    def set_email(self, email):
        self.set_text(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Заполняем "Пароль"')
    def set_password(self, password):
        self.set_text(LoginPageLocators.PASSWORD_FIELD, password)
