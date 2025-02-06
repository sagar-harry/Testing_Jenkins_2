
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class ShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com/login")  # Replace with the actual URL

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def test_shopping_cart_reset_functionality(self):
        driver = self.driver
        
        # Log in to the application
        self.login("standard_user", "secret_sauce")

        # Add 'Bike Light' to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Add 'Fleece Jacket' to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Verify cart badge displays '2'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, "2", "Cart badge does not display '2'")

        # Reset the cart
        driver.find_element(By.ID, "reset_sidebar_link").click()

        # Verify the cart is empty
        cart_badge_elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(len(cart_badge_elements), 0, "Cart is not empty after reset")

        # Add 'Bolt T-Shirt' to the cart after reset
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Verify cart badge displays '1'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, "1", "Cart badge does not display '1' after reset")

if __name__ == "__main__":
    unittest.main()
