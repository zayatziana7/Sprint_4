import allure
from selenium.webdriver.common.by import By

from framework.helpers import locator_helper
from page_objects.locators.important_questions_locators import ImportantQuestionsLocators
from page_objects.pages.base_page import BasePage


class ImportantQuestionsPage(BasePage):

    @allure.step('Получаем аккордион из блока с важными вопросами')
    def get_accordion_element(self, question_number: str | int, answer: bool = False):
        if answer:
            current_answer_locator = locator_helper.build_locator(ImportantQuestionsLocators.ACCORDION_WITH_ANSWER,
                                                                  question_number)
            return self.find_element(locator=(By.XPATH, current_answer_locator))
        current_question_locator = locator_helper.build_locator(ImportantQuestionsLocators.ACCORDION_WITH_QUESTION,
                                                                question_number)
        return self.find_element(locator=(By.XPATH, current_question_locator))
