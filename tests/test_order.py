import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.test_data import TestData


class TestOrder:
    """Тесты для заказа самоката"""

    def test_order_from_top_button(self, driver):
        """Заказ через кнопку 'Заказать' (сверху)"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        data = TestData.ORDER_1
        order_page.fill_first_form(data["name"], data["surname"], data["address"], data["metro"], data["phone"])
        order_page.fill_second_form(data["date"], data["rental_period"], data["color"], data["comment"])
        order_page.confirm_order()

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

    def test_order_from_bottom_button(self, driver):
        """Заказ через кнопку 'Заказать' (снизу)"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        data = TestData.ORDER_2
        order_page.fill_first_form(data["name"], data["surname"], data["address"], data["metro"], data["phone"])
        order_page.fill_second_form(data["date"], data["rental_period"], data["color"], data["comment"])
        order_page.confirm_order()

        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message