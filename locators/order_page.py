from selenium.webdriver.common.by import By


class OrderPageLocators:
    COUNTER_DONE_ALL_TIME = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed')]"
    COUNTER_DONE_TODAY = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed')]"
    ORDERS_IN_PROGRESS = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='{}']"
