from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы оформления заказа"""

    # Первая форма
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_ARROW = (By.CLASS_NAME, "Dropdown-arrow")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")

    # Подтверждение
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Шаблоны (динамические)
    METRO_OPTION_TEMPLATE = (By.XPATH, "//div[text()='{}']")
    RENTAL_OPTION_TEMPLATE = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and contains(text(), '{}')]")