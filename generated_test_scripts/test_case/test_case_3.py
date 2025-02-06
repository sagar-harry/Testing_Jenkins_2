
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "#user-name"
        self.password_locator = "#password"
        self.login_button_locator = "#login-button"
    
    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, self.username_locator).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, self.password_locator).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_locator).click()

class CartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
    
    def test_cart_operations(self):
        driver = self.driver
        
        # Add Bike Light and Fleece Jacket to the cart
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket").click()
        
        # Verify cart badge displays '2'
        cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
        self.assertEqual(cart_badge.text, "2", "Cart badge should display '2'")
        
        # Reset the cart
        driver.find_element(By.CSS_SELECTOR, "#reset_sidebar_link").click()
        
        # Verify the cart is empty
        cart_badges = driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
        self.assertTrue(len(cart_badges) == 0, "Cart should be empty")
        
        # Add Bolt T-Shirt to the cart after reset
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        
        # Verify cart badge displays '1'
        cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
        self.assertEqual(cart_badge.text, "1", "Cart badge should display '1'")
    
    def tearDown(self):
        time.sleep(2)  # For demonstration purposes. Remove in real test scenarios
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
