from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Page Object для главной страницы Яндекс.Самокат"""

    URL = "https://qa-scooter.education-services.ru/"

    def open_main_page(self):
        """Открыть главную страницу"""
        self.open(self.URL)

    def click_order_button_top(self):
        """Клик по кнопке 'Заказать' (сверху)"""
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        """Клик по кнопке 'Заказать' (снизу)"""
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_question(self, question_number):
        """Клик по вопросу в аккордеоне (0-7)"""
        from selenium.webdriver.common.by import By
        locator = (By.ID, f"accordion__heading-{question_number}")
        self.click(locator)

    def get_answer_text(self, answer_number):
        """Получить текст ответа (0-7)"""
        from selenium.webdriver.common.by import By
        locator = (By.ID, f"accordion__panel-{answer_number}")
        return self.get_text(locator)