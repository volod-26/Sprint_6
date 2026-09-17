import pytest
from pages.main_page import MainPage


class TestQuestions:
    """Тесты для раздела «Вопросы о важном»"""

    @pytest.mark.parametrize("question_number, expected_text", [
        (0, "Сутки"),
        (1, "один заказ"),
        (2, "8 мая"),
        (3, "завтрашнего дня"),
        (4, "1010"),
        (5, "восемь суток"),
        (6, "объяснительной"),
        (7, "Москве"),
    ])
    def test_question_opens_answer(self, driver, question_number, expected_text):
        """Тест: при клике на вопрос открывается соответствующий ответ"""
        page = MainPage(driver)
        page.open()
        page.click_question(question_number)
        actual_text = page.get_answer_text(question_number)
        assert expected_text in actual_text