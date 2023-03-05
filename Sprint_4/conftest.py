import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

import config
from page_objects.locators.base_page_locators import BasePageLocators
from page_objects.pages.base_page import BasePage
from page_objects.pages.important_questions_page import ImportantQuestionsPage
from page_objects.pages.order_page import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(config.APP_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver)


@pytest.fixture
def important_questions_page(driver):
    important_questions_page = ImportantQuestionsPage(driver)
    important_questions_page.scroll_to_the_bottom()
    return important_questions_page


@pytest.fixture
def open_order_page(base_page, by_bottom_button=False):
    if not by_bottom_button:
        base_page.find_element(BasePageLocators.TOP_ORDER_BUTTON).click()
    else:
        base_page.scroll_to_the_bottom()
        base_page.find_element(BasePageLocators.BOTTOM_ORDER_BUTTON).click()
    return OrderPage(base_page.driver)
