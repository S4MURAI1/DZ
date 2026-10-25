from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)  # ждём до 10 секунд

    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")
        original_url = driver.current_url

        name_field = wait.until(EC.presence_of_element_located((By.NAME, "custname")))
        name_field.send_keys("Sergey")

        # Ищем кнопку: пробуем несколько селекторов, пока не найдём
        submit_button = None
        selectors = [
            (By.XPATH, '//button[contains(text(), "Submit")]'),
            (By.XPATH, '//input[@type="submit" and @value="Submit"]'),
            (By.XPATH, '//*[contains(text(), "Submit")]'),
        ]

        for by, value in selectors:
            try:
                submit_button = wait.until(EC.element_to_be_clickable((by, value)))
                break
            except:
                continue

        if submit_button is None:
            raise RuntimeError("Кнопка Submit не найдена")

        submit_button.click()

        wait.until(lambda d: d.current_url != original_url)

    finally:
        driver.quit()
