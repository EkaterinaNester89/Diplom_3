import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.common import URLS
from locators.home_page import HomePageLocators


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

    @allure.step(f"Заходим страницу {URLS.LOGIN_PAGE}")
    def open_login_page(self):
        self.open_url(URLS.LOGIN_PAGE)

    @allure.step("Нажимаем на элемент")
    def click_to_element(self, locator, seconds=3):
        element = WebDriverWait(self.driver, seconds).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Ожидаем отображение элемента")
    def wait_element_visibility_of_element_located(self, locator, seconds=3):
        return WebDriverWait(self.driver, seconds).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидаем кликабельность элемента")
    def wait_element_to_be_clickable(self, locator, seconds=3):
        return WebDriverWait(self.driver, seconds).until(
            EC.element_to_be_clickable(locator)
        )
    @allure.step("Ищем элемент по локатору")
    def find_element(self, locator, seconds=5):
        return self.wait_element_visibility_of_element_located(locator, seconds=seconds)

    @allure.step("Переносим элемент")
    def drag_and_drop(self, source_element, destination_element):
        js_script = """
         function createEvent(typeOfEvent) {
             var event = document.createEvent("CustomEvent");
             event.initCustomEvent(typeOfEvent, true, true, null);
             event.dataTransfer = {
                 data: {},
                 setData: function(key, value) {
                     this.data[key] = value;
                 },
                 getData: function(key) {
                     return this.data[key];
                 }
             };
             return event;
         }

         function dispatchEvent(element, event, transferData) {
             if (transferData !== undefined) {
                 event.dataTransfer = transferData;
             }
             if (element.dispatchEvent) {
                 element.dispatchEvent(event);
             } else if (element.fireEvent) {
                 element.fireEvent("on" + event.type, event);
             }
         }

         var source = arguments[0];
         var target = arguments[1];

         var dragStartEvent = createEvent('dragstart');
         dispatchEvent(source, dragStartEvent);

         var dropEvent = createEvent('drop');
         dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);

         var dragEndEvent = createEvent('dragend');
         dispatchEvent(source, dragEndEvent, dropEvent.dataTransfer);
         """

        self.driver.execute_script(js_script, source_element, destination_element)

    @allure.step("Получаем текст элемента")
    def get_text(self, locator, seconds=3):
        element = self.find_element(locator, seconds)
        return element.text

    @allure.step("Вводим текст")
    def set_text(self, locator, text, seconds=3):
        element = self.find_element(locator, seconds)
        return element.send_keys(text)
