from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Открываем GitFlic
        driver.get("https://gitflic.ru/")

        # Cookie пользователя 1
        driver.add_cookie({
            "name": "SESSION",
            "value": "NDkwZDE5ZjYtNzI5Yy00NjFhLWJiNDYtNGUxNGZlOTAwOTNj",
            "path": "/"
        })

        # Обновляем страницу
        driver.refresh()

        # Переходим в профиль пользователя 1
        driver.get("https://gitflic.ru/user/airsworld")

        # Сохраняем URL пользователя 1
        url_user_1 = driver.current_url

        # Очищаем cookie
        driver.delete_all_cookies()

        # Cookie пользователя 2
        driver.add_cookie({
            "name": "SESSION",
            "value": "ZDJhNDcyODUtNWI3Yy00ZjI4LTk1MDYtYTZiZTAyY2NjMzBi",
            "path": "/"
        })

        # Обновляем страницу
        driver.refresh()

        # Переходим в профиль пользователя 2
        driver.get("https://gitflic.ru/user/s4murai")

        # Сохраняем URL пользователя 2
        url_user_2 = driver.current_url

        # Проверяем, что URL отличаются
        assert url_user_1 != url_user_2

    finally:
        driver.quit()