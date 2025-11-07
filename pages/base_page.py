import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.common import URLS


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем ссылку")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step(f"Открываем страницу {URLS.HOME_PAGE}")
    def open_home_page(self):
        self.open_url(URLS.HOME_PAGE)

    @allure.step("Нажимаем на элемент")
    def click_to_element(self, locator, seconds=3):
        element = WebDriverWait(self.driver, seconds).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
