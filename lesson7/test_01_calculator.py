from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)
        page.open()
        page.set_delay(45)

        for button in ("7", "+", "8", "="):
            page.click_button(button)

        result = page.get_result()
    finally:
        driver.quit()

    assert result == "15"
