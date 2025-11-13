# Diplom 3 develop_3 Автотесты stellar burgers Selenium Allure


В проекте зайдествованы автотесты для проверки сервиса stellar burgers с помощью Selenium, Pytest и Allure.
Автотесты реализованы по паттерну Page Object.


## Установка и запуск

Установка зависимостей:

`pip install -r requirements.txt`

Запуск тестов:

`pytest -v`


Запуск автотестов и создание отчета о тестировании в Allure:

`pytest --alluredir=allure_results`

Создание отчета из результатов тестов:

`allure serve ./allure_results`

Генерация отчета из результатов тестов:

`allure generate ./allure_results/ -o allure_report `


## Структура проекта

- Diplom_3/
  - allure_report/ # сгенерированный отчет
  - allure_results/ # сгенерированные файлы до отчета
  - data/ # данные для использования в тестах
  - helpers/ # классы c действиями для разных ручек для данных полученных по API
  - locators/ # свойства поиска элементов для разных страниц
  - pages/ # Page Object классы c действиями для разных страниц сайта
  - tests/  # Тесты, сгруппированные по функционалу
  - conftest.py # Фикстуры Pytest
  - pytest.ini # настройки pytest 
  - README.md # Текущий файл
  - requirements.txt # Зависимости проекта

  

Автор: Нестер Екатерина Васильевна
https://github.com/EkaterinaNester89/