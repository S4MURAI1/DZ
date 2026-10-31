from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_checkout():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Открываем сайт
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавляем товары в корзину
        products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]

        for product in products:
            wait.until(
                EC.element_to_be_clickable((By.ID, product))
            ).click()

        # Переходим в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Нажимаем Checkout
        wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        # Заполняем данные покупателя
        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Sergey")

        driver.find_element(By.ID, "last-name").send_keys("Ivanov")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # Нажимаем Continue
        driver.find_element(By.ID, "continue").click()

        # Получаем итоговую стоимость
        total_element = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )

        total = total_element.text

        print("Итоговая стоимость:", total)

        # Проверяем итоговую сумму
        assert total == "Total: $58.29"

    finally:
        # Закрываем браузер
        driver.quit()
