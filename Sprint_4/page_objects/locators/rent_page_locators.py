from selenium.webdriver.common.by import By


class RentPageLocators:
    DATE_TO_DELIVER_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_FIELD = (By.XPATH, "//div[@class='Dropdown-arrow-wrapper']/span")
    RENT_TIMES_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-menu']/div")
    BLACK_SCOOTER_COLOR_CHECKBOX = (By.XPATH, "//input[@id='black']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[contains(text(), 'Заказать')]")
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    ORDER_CREATED_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
