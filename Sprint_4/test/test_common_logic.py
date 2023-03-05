import config
from data import constants


class TestCommonLogic:
    def test_user_can_go_to_app_home_page_from_header(self, open_order_page):
        open_order_page.click_on_app_name_from_header()

        assert open_order_page.get_current_url() == config.APP_URL, 'Редирект на домашнюю страницу приложения' \
                                                                    ' отработал некорректно!'

    def test_user_can_go_to_yandex_home_page_from_header(self, base_page):
        base_page.click_on_yandex_name_from_header()
        base_page.switch_tab()

        assert base_page.get_current_url() == constants.YANDEX_HOME_PAGE_URL, 'Редирект на домашнюю страницу Яндекса' \
                                                                              ' отработал некорректно!'
