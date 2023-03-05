import pytest

from framework.entities import order_data
from page_objects.locators.rent_page_locators import RentPageLocators


class TestCreateScooterOrder:
    @pytest.mark.parametrize('by_bottom_button', [False, True])
    def test_create_order(self, open_order_page, by_bottom_button):
        open_order_page.fill_order_form(order_data=order_data.default_order)
        rent_page = open_order_page.click_next_button()

        rent_page.fill_rent_page(rent_data=order_data.default_order.rent_data)
        rent_page.order_scooter()
        rent_page.submit_ordering()

        assert open_order_page.find_element(RentPageLocators.ORDER_CREATED_MODAL), \
            'Заказ не был создан!'
