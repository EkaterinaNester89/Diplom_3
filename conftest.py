import allure
import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    allure.dynamic.parameter("browser", browser_name)

    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер не поддерживается: {request.param}")

    driver.maximize_window()
    yield driver
    driver.quit()
