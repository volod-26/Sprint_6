import pytest
from pages.main_page import MainPage
from data.test_data import TestData


class TestQuestions:
    """Тесты для раздела «Вопросы о важном»"""

    @pytest.mark.parametrize("question_number, expected_text", TestData.QUESTIONS_ANSWERS)
    def test_question_opens_answer(self, driver, question_number, expected_text):
        """Тест: при клике на вопрос открывается соответствующий ответ"""
        page = MainPage(driver)
        page.open_main_page()
        page.click_question(question_number)
        actual_text = page.get_answer_text(question_number)
        assert expected_text in actual_text