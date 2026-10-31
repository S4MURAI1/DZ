from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    PRODUCTS = {
        "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self, product_name):
        button_id = self.PRODUCTS[product_name]
        self.wait.until(
            EC.element_to_be_clickable((By.ID, button_id))
        ).click()

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
