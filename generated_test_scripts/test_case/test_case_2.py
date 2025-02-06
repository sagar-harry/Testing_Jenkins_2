
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        self.login_page = LoginPage(self.driver)

    def test_cart_count(self):
        # Step 1: Log in using the Login method
        self.login_page.login("standard_user", "secret_sauce")
        
        # Step 2: Add 'Bike Light' to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        
        # Step 3: Add 'Fleece Jacket' to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        
        # Step 4: Validate if the cart badge displays '2'
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "2", "Cart badge does not display the correct count.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
