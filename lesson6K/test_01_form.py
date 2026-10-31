from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Открываем страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        # Данные для заполнения формы
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        # Заполняем все поля
        for field_id, value in fields.items():
            element = wait.until(
                EC.visibility_of_element_located(
                    (By.NAME, field_id)
                )
            )
            element.send_keys(value)

        # Нажимаем кнопку Submit
        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        # Ждём появления результатов проверки
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "zip-code")
            )
        )

        # Проверяем Zip code (красный)
        zip_code = driver.find_element(By.ID, "zip-code")

        assert "alert-danger" in zip_code.get_attribute("class")

        # Проверяем остальные поля (зелёные)
        for field_id in fields:
            element = driver.find_element(By.ID, field_id)

            assert "alert-success" in element.get_attribute("class")

    finally:
        # Закрываем браузер
        driver.quit()
