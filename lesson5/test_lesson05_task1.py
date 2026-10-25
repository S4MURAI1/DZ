from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()

    # 1. Открываем главную страницу
    driver.get("https://httpbin.qa-territory.online")
    original_url = driver.current_url

    # 2. Находим ссылку "HTML Form" по тексту и кликаем
    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    # 3. Проверяем, что URL изменился на /forms/post
    current_url = driver.current_url
    assert "/forms/post" in current_url, f"Ожидался URL с /forms/post, но получен: {current_url}"

    # 4. Возвращаемся назад
    driver.back()

    # 5. Проверяем, что вернулись на исходный URL
    back_url = driver.current_url
    assert back_url == original_url, f"Ожидался исходный URL: {original_url}, но получен: {back_url}"

    driver.quit()
    