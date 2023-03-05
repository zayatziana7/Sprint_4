from selenium.webdriver.common.by import By


class BasePageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Header')]//button[contains(text(), 'Заказать')]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_RoadMap')]//button[contains(text(), 'Заказать')]")
    APP_LOGO_BUTTON = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO_BUTTON = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
