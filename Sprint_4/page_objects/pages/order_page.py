import allure

from framework.entities.order_data import OrderData
from page_objects.locators.base_page_locators import BasePageLocators
from page_objects.locators.order_page_locators import OrderPageLocators
from page_objects.pages.base_page import BasePage
from page_objects.pages.rent_page import RentPage


class OrderPage(BasePage):

    @allure.step('Открываем страницу создания заказа')
    def open_order_page(self, by_bottom_button: bool = False):
        if not by_bottom_button:
            self.find_elements(BasePageLocators.TOP_ORDER_BUTTON)[0].click()
        else:
            self.find_elements(BasePageLocators.TOP_ORDER_BUTTON)[1].click()

    @allure.step('Заполняем форму создания заказа')
    def fill_order_form(self, order_data: OrderData):
        self.fill_field(OrderPageLocators.NAME_INPUT, order_data.name)
        self.fill_field(OrderPageLocators.SURNAME_INPUT, order_data.surname)
        self.fill_field(OrderPageLocators.ADDRESS_INPUT, order_data.address)
        self.find_element(OrderPageLocators.METRO_STATION_INPUT).click()
        self.find_element(OrderPageLocators.METRO_STATIONS_DROPDOWN).click()
        self.fill_field(OrderPageLocators.PHONE_NUMBER_INPUT, order_data.phone_number)

    @allure.step('Нажимаем "Далее"')
    def click_next_button(self):
        self.find_element(OrderPageLocators.NEXT_BUTTON).click()
        return RentPage(self.driver)
