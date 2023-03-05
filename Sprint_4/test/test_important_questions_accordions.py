import pytest

from framework.checkers import common_checkers
from framework.entities.important_question_accordion import all_accordions


class TestImportantQuestionsAccordions:
    @pytest.mark.parametrize('accordion', [*all_accordions])
    def test_user_can_open_accordion_with_question(self, important_questions_page, accordion):
        question_element = important_questions_page.get_accordion_element(question_number=accordion.number)

        important_questions_page.click_on_element_via_action_chains(question_element)

        answer_element = important_questions_page.get_accordion_element(question_number=accordion.number, answer=True)

        common_checkers.check_element_text(expected_text=accordion.question,
                                           actual_text=important_questions_page.get_element_text(question_element))
        common_checkers.check_element_text(expected_text=accordion.answer,
                                           actual_text=important_questions_page.get_element_text(answer_element))
