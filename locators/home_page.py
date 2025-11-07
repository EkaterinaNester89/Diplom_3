from selenium.webdriver.common.by import By


class HomePageLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, "//nav//a//p[text()='Конструктор']"
    FEED_BUTTON = By.XPATH, "//nav//a//p[text()='Лента Заказов']"
    INGREDIENT = By.XPATH, "//ul[contains(@class, 'BurgerIngredients_ingredients__list')]/a[contains(@class, 'BurgerIngredient_ingredient')]"
    INGREDIENT_DETAILS_MODAL = By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//h2[text()= 'Детали ингредиента']",
    INGREDIENT_DETAILS_MODAL_CLOSE_BUTTON = By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//button[contains(@class, 'Modal_modal__close_modified')]",

