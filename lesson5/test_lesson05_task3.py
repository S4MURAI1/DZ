from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_multiple_elements():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online/links/10")

        # Ждём, пока появятся все ссылки (хотя бы одна уже есть — значит, список можно собирать)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))

        # Находим ВСЕ ссылки на странице
        links = driver.find_elements(By.TAG_NAME, "a")

        # 1. Проверяем, что количество ссылок равно 9
        assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено: {len(links)}"

        # 2. Проверяем, что все ссылки отображаются на странице
        for link in links:
            assert link.is_displayed(), "Одна из ссылок не отображается на странице"

        # 3. Проверяем, что текст первой ссылки содержит "1"
        first_link_text = links[0].text
        assert "1" in first_link_text, f"Текст первой ссылки не содержит '1': {first_link_text}"

    finally:
        driver.quit()
