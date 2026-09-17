from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """Page Object для главной страницы Яндекс.Самокат"""

    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Middle')]")

    # Логотипы
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открыть главную страницу"""
        self.driver.get("https://qa-scooter.education-services.ru/")

    def click_order_button_top(self):
        """Клик по кнопке 'Заказать' (сверху)"""
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_TOP)).click()

    def click_order_button_bottom(self):
        """Клик по кнопке 'Заказать' (снизу)"""
        button = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_BOTTOM))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script("arguments[0].click();", button)

    def click_question(self, question_number):
        """Клик по вопросу в аккордеоне (0-7)"""
        locator = (By.ID, f"accordion__heading-{question_number}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, answer_number):
        """Получить текст ответа (0-7)"""
        locator = (By.ID, f"accordion__panel-{answer_number}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text