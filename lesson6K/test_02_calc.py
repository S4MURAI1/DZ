from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_calculator():
    browser = webdriver.Chrome()
    try:
        browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        # Создаем ожидание до 50 секунд
        wait = WebDriverWait(browser, 50)
        # Находим поле задержки и вводим 45 секунд
        delay = browser.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys("45")
        # Нажимаем кнопки калькулятора
        browser.find_element(By.XPATH, "//span[text()='7']").click()
        browser.find_element(By.XPATH, "//span[text()='+']").click()
        browser.find_element(By.XPATH, "//span[text()='8']").click()
        browser.find_element(By.XPATH, "//span[text()='=']").click()
        # Ожидаем появления результата 15
        result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        assert result is True
    finally:
        browser.quit()
