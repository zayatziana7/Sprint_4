def build_locator(locator: str, value: str | int):
    if not isinstance(value, str):
        value = str(value)
    return locator.format(value)
