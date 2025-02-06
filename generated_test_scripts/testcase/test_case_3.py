
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")
        time.sleep(2)  # Wait for login, adjust according to network conditions

    def test_shopping_cart(self):
        driver = self.driver

        # Add 'Bike Light' to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()

        # Add 'Fleece Jacket' to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        # Check if cart displays '2'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        self.assertEqual(cart_count, '2')

        # Reset the cart (remove added products)
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()

        # Verify the cart is empty
        cart_count_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        if cart_count_elements:
            cart_count = cart_count_elements[0].text
            self.assertEqual(cart_count, '', "Cart should be empty but is not.")

        # Add 'Bolt T-Shirt' to cart after reset
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(1)  # Wait for any animations or DOM changes

        # Check if cart displays '1'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        self.assertEqual(cart_count, '1')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
