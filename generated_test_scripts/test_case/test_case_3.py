
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class ShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")  # Replace with the actual URL
        # Assuming LoginPage class and login method are already defined
        self.login_page = LoginPage(self.driver)  
        self.login_page.login("user", "password")  # Replace with actual user credentials

    def test_shopping_cart(self):
        driver = self.driver

        # Add 'Bike Light' to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Add 'Fleece Jacket' to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Verify the cart badge shows '2'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, "2")

        # Reset the cart
        driver.find_element(By.ID, "reset_sidebar_link").click()

        # Verify the cart is empty
        cart_badge_elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(len(cart_badge_elements), 0)

        # Add 'Bolt T-Shirt' to the cart after reset
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        # Verify the cart badge shows '1'
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, "1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

Note: Ensure the `LoginPage` class and its `login` method are defined elsewhere in your project to handle the login functionality. The URL, user credentials, and locators (`ID`s) should be replaced with the actual ones from your application.