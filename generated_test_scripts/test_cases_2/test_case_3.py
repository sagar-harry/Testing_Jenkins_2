
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class UITestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')

    def test_add_products_and_reset_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Add Bike Light to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        
        # Add Fleece Jacket to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Validate cart badge displays '2'
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, "2")

        # Reset the cart
        self.driver.find_element(By.ID, "reset_sidebar_link").click()

        # Validate cart is empty
        cart_badge_elements = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(len(cart_badge_elements), 0)

        # Add Bolt T-Shirt to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        
        # Validate cart badge displays '1'
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_badge, "1")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
