from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открываем учебную страницу (вместо gitflic.ru)
        driver.get("https://the-internet.herokuapp.com/cookie/simple")

        # --- Пользователь 1 (имитация) ---
        # Добавляем простую куку, которая означает «пользователь 1»
        driver.add_cookie({"name": "user_id", "value": "101", "domain": "the-internet.herokuapp.com"})
        driver.refresh()

        # Сохраняем URL и текст, который зависит от куки
        url_user1 = driver.current_url
        content_text_1 = wait.until(EC.visibility_of_element_located((By.ID, "content"))).text

        # --- Разлогин (очистка кук) ---
        driver.delete_all_cookies()
        driver.refresh()

        # --- Пользователь 2 (имитация) ---
        # Добавляем куку для «пользователя 2»
        driver.add_cookie({"name": "user_id", "value": "202", "domain": "the-internet.herokuapp.com"})
        driver.refresh()

        # Сохраняем URL и текст для пользователя 2
        url_user2 = driver.current_url
        content_text_2 = wait.until(EC.visibility_of_element_located((By.ID, "content"))).text

        # Проверка: URL могут совпадать (страница одна), но состояние должно быть разным
        assert url_user1 == url_user2, "На этой странице URL всегда одинаковый — это нормально"
        assert content_text_1 != content_text_2, f"Содержимое должно отличаться: {content_text_1} vs {content_text_2}"

    finally:
        driver.quit()
