from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop_total():
    driver = webdriver.Chrome()
    try:
        LoginPage(driver).open().login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_product("Sauce Labs Backpack")
        inventory.add_product("Sauce Labs Bolt T-Shirt")
        inventory.add_product("Sauce Labs Onesie")
        inventory.open_cart()

        cart = CartPage(driver)
        expected_products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]
        assert sorted(cart.get_item_names()) == sorted(expected_products)

        cart.checkout()

        checkout = CheckoutPage(driver)
        # Замените значения на свои данные перед запуском.
        checkout.fill_information("Ivan", "Ivanov", "12345")
        total = checkout.get_total()
    finally:
        driver.quit()

    assert total == 58.29
