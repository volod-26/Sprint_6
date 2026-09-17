import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    """Тесты для заказа самоката"""

    @pytest.mark.parametrize(
        "entry_point, name, surname, address, metro, phone, date, rental_period, color, comment",
        [
            # Набор данных 1: кнопка сверху
            ("top", "Иван", "Иванов", "Москва, ул. Ленина, 1", "Черкизовская",
             "+79991112233", "15.09.2026", "сутки", "black", "Позвоните за час"),
            # Набор данных 2: кнопка снизу
            ("bottom", "Пётр", "Петров", "Москва, ул. Пушкина, 10", "Сокольники",
             "+79994445566", "16.09.2026", "двое суток", "grey", "Оставьте у подъезда"),
        ]
    )
    def test_order_scooter_positive(self, driver, entry_point, name, surname, address,
                                     metro, phone, date, rental_period, color, comment):
        """Тест: позитивный сценарий заказа самоката"""
        main_page = MainPage(driver)
        main_page.open()

        # Точка входа: кнопка сверху или снизу
        if entry_point == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        # Заполняем формы заказа
        order_page = OrderPage(driver)
        order_page.fill_first_form(name, surname, address, metro, phone)
        order_page.fill_second_form(date, rental_period, color, comment)
        order_page.confirm_order()

        # Проверяем сообщение об успехе
        success_message = order_page.get_success_message()
        assert "Заказать" in success_message or "Заказ оформлен" in success_message