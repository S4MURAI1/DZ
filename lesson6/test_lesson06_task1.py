from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_dynamic_loading():
    # Настраиваем драйвер
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)  # ждём до 10 секунд

    try:
        # 1. Открываем страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Находим и нажимаем кнопку "Start" (используем CSS-селектор)
        start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.example button")))
        start_button.click()

        # 3. Ждём появления текста "Hello World!"
        # Ищем элемент, который содержит нужный текст
        hello_world_element = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        # 4. Делаем скриншот страницы
        screenshot_path = os.path.join(os.getcwd(), "dynamic_loading_screenshot.png")
        driver.save_screenshot(screenshot_path)
        # Скриншот сохранится в текущей рабочей директории (обычно корень проекта)

        # 5. Проверяем, что текст равен "Hello World!"
        assert hello_world_element.text == "Hello World!", f"Ожидался 'Hello World!', но получен: {hello_world_element.text}"

    finally:
        driver.quit()
