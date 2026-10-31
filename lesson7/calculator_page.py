from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT = (By.CSS_SELECTOR, ".screen")
    BUTTON = lambda self, value: (
        By.XPATH,
        f"//span[normalize-space()='{value}']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds):
        field = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, value):
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON(value))
        )
        button.click()

    def get_result(self):
        return self.wait.until(
            lambda driver: (
                driver.find_element(*self.RESULT).text
                if driver.find_element(*self.RESULT).text.strip() == "15"
                else False
            )
        )
