from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    """Page Object для страницы оформления заказа"""

    def fill_first_form(self, name, surname, address, metro, phone):
        """Заполнить первую форму заказа"""
        self.fill(OrderPageLocators.NAME_INPUT, name)
        self.fill(OrderPageLocators.SURNAME_INPUT, surname)
        self.fill(OrderPageLocators.ADDRESS_INPUT, address)
        self.click(OrderPageLocators.METRO_INPUT)
        self.fill(OrderPageLocators.METRO_INPUT, metro)
        metro_option = (OrderPageLocators.METRO_OPTION_TEMPLATE[0],
                        OrderPageLocators.METRO_OPTION_TEMPLATE[1].format(metro))
        self.click(metro_option)
        self.fill(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, date, rental_period, color, comment):
        """Заполнить вторую форму заказа"""
        # Дата
        self.fill(OrderPageLocators.DATE_INPUT, date)

        # Срок аренды
        self.click(OrderPageLocators.RENTAL_ARROW)
        rental_option = (OrderPageLocators.RENTAL_OPTION_TEMPLATE[0],
                         OrderPageLocators.RENTAL_OPTION_TEMPLATE[1].format(rental_period))
        self.click(rental_option)

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