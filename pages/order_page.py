import time
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    """Page Object для страницы оформления заказа"""

    def fill_first_form(self, name, surname, address, metro, phone):
        """Заполнить первую форму заказа"""
        self.fill(OrderPageLocators.NAME_INPUT, name)
        self.fill(OrderPageLocators.SURNAME_INPUT, surname)
        self.fill(OrderPageLocators.ADDRESS_INPUT, address)
        self.click(OrderPageLocators.METRO_INPUT)
        self.fill(OrderPageLocators.METRO_INPUT, metro)
        self.click((By.XPATH, f"//div[text()='{metro}']"))
        self.fill(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, date, rental_period, color, comment):
        """Заполнить вторую форму заказа"""
        # Дата
        self.fill(OrderPageLocators.DATE_INPUT, date)
        time.sleep(1)

        # Срок аренды — клик по стрелке
        self.click(OrderPageLocators.RENTAL_ARROW)
        time.sleep(1)
        self.click((By.XPATH, f"//div[contains(@class, 'Dropdown-option') and contains(text(), '{rental_period}')]"))
        time.sleep(1)

        # Цвет
        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)

        # Комментарий
        self.fill(OrderPageLocators.COMMENT_INPUT, comment)

        # Кнопка "Заказать"
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        """Подтвердить заказ"""
        self.click(OrderPageLocators.YES_BUTTON)

    def get_success_message(self):
        """Получить текст сообщения об успехе"""
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)