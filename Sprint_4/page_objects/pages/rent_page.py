import allure

from framework.entities.rent_data import RentData
from page_objects.locators.rent_page_locators import RentPageLocators
from page_objects.pages.base_page import BasePage


class RentPage(BasePage):

    @allure.step('Заполняем форму с информацией по аренде')
    def fill_rent_page(self, rent_data: RentData):
        self.fill_field(RentPageLocators.DATE_TO_DELIVER_INPUT, rent_data.date_to_deliver)
        self.find_element(RentPageLocators.RENT_TIME_FIELD).click()
        self.find_elements(RentPageLocators.RENT_TIMES_DROPDOWN)[0].click()
        self.find_element(RentPageLocators.BLACK_SCOOTER_COLOR_CHECKBOX).click()
        if rent_data.comment:
            self.fill_field(RentPageLocators.COMMENT_INPUT, rent_data.comment)

    @allure.step('Делаем заказ')
    def order_scooter(self):
        self.find_element(RentPageLocators.ORDER_BUTTON).click()

    @allure.step('Подтверждаем заказ')
    def submit_ordering(self):
        self.find_element(RentPageLocators.SUBMIT_ORDER_BUTTON).click()
