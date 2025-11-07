import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    @allure.step("Открываем ссылку")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url
