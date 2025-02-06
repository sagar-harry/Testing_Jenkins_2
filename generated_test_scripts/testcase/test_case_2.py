
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")  # Replace with the actual URL of the application
        time.sleep(3)

    def test_add_items_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        # Add 'Bike Light' to cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Verify cart count
        cart_count = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        self.assertEqual(cart_count, '2')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
