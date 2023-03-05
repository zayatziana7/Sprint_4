import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import config
from page_objects.locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url=config.APP_URL, timeout_in_seconds: int = 10):
        self.url = url
        self.driver = driver
        self.timeout_in_seconds = timeout_in_seconds

    @allure.step('Ищем элемент по локатору')
    def find_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, self.timeout_in_seconds) \
            .until(ec.visibility_of_element_located(locator))

    @allure.step('Ищем элементы по локатору')
    def find_elements(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    @allure.step('Кликаем по элементу')
    def click_on_element(self, element: WebElement):
        element.click()

    @allure.step('Кликаем по элементу через ActionChains')
    def click_on_element_via_action_chains(self, element: WebElement):
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Получаем текст из элемента')
    def get_element_text(self, element: WebElement) -> str:
        text = element.text
        if not text:
            text = element.get_attribute('value')
        return text

    @allure.step('Скроллим страницу в самый низ')
    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Заполняем инпут-поле')
    def fill_field(self, locator: tuple, value: str):
        element = self.find_element(locator)
        element.send_keys(value)

    @allure.step('Кликаем по лого приложения в хедере')
    def click_on_app_name_from_header(self):
        self.find_element(BasePageLocators.APP_LOGO_BUTTON).click()

    @allure.step('Кликаем по лого Яндекса в хедере')
    def click_on_yandex_name_from_header(self):
        self.find_element(BasePageLocators.YANDEX_LOGO_BUTTON).click()

    @allure.step('Получаем url текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключаемся на соседнюю вкладку в браузере')
    def switch_tab(self):
        current_tab = self.driver.current_window_handle
        all_tabs = self.driver.window_handles
        for tab in all_tabs:
            if tab != current_tab:
                self.driver.switch_to.window(tab)
        time.sleep(1)
