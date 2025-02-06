
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        user_input = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "#password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "#login-button")
        
        user_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

class UITests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_add_items_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        
        bike_light_button = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
        fleece_jacket_button = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
        
        bike_light_button.click()
        fleece_jacket_button.click()
        
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, '2', "Cart badge does not show the correct item count.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
