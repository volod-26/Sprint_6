import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    """Page Object для страницы оформления заказа"""

    # Первая форма заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_ARROW = (By.CLASS_NAME, "Dropdown-arrow")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")

    # Подтверждение заказа
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_first_form(self, name, surname, address, metro, phone):
        """Заполнить первую форму заказа"""
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.METRO_INPUT).click()
        self.driver.find_element(*self.METRO_INPUT).send_keys(metro)
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[text()='{metro}']"))).click()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_second_form(self, date, rental_period, color, comment):
        """Заполнить вторую форму заказа"""
        # 1. Вводим дату
        date_input = self.wait.until(EC.visibility_of_element_located(self.DATE_INPUT))
        date_input.send_keys(date)
        date_input.send_keys("\n")
        time.sleep(1)

        # 2. Открываем выпадающий список срока аренды — клик по стрелке
        arrow = self.wait.until(EC.presence_of_element_located(self.RENTAL_ARROW))
        self.driver.execute_script("arguments[0].click();", arrow)
        time.sleep(1)

        # 3. Выбираем опцию по тексту
        option = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and contains(text(), '{rental_period}')]")))
        self.driver.execute_script("arguments[0].click();", option)
        time.sleep(1)

        # 4. Выбираем цвет
        if color == "black":
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*self.COLOR_GREY).click()

        # 5. Комментарий
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

        # 6. Кнопка "Заказать"
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()

    def confirm_order(self):
        """Подтвердить заказ"""
        self.wait.until(EC.element_to_be_clickable(self.YES_BUTTON)).click()

    def get_success_message(self):
        """Получить текст сообщения об успехе"""
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text