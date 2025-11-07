from selenium.webdriver.common.by import By


class HomePageLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, "//nav//a//p[text()='Конструктор']"
    FEED_BUTTON = By.XPATH, "//nav//a//p[text()='Лента Заказов']"
