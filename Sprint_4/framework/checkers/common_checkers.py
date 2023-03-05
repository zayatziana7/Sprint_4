import allure


@allure.step('Проверяем, что ожидаемый текст совпадает с фактическим')
def check_element_text(expected_text: str, actual_text: str):
    assert expected_text == actual_text, f'Expected text {expected_text}' \
                                         f' is not the same as the actual text {actual_text}!'
