
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestAddToCart(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.example.com')  # replace with actual URL

    def tearDown(self):
        self.driver.quit()

    def test_add_items_to_cart(self):
        driver = self.driver
        self.login()  # Use login method in LoginPage
        
        # Add 'Bike Light' to the cart
        bike_light_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
        bike_light_button.click()

        # Add 'Fleece Jacket' to the cart
        fleece_jacket_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
        fleece_jacket_button.click()
        
        # Check if cart badge displays '2'
        cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        self.assertEqual(cart_badge.text, '2', "Cart badge does not display the correct count")
    
    def login(self):
        driver = self.driver
        username_input = driver.find_element(By.ID, 'user-name')
        password_input = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.ID, 'login-button')
        
        username_input.send_keys('standard_user')  # replace with actual username
        password_input.send_keys('secret_sauce')  # replace with actual password
        login_button.click()

if __name__ == '__main__':
    unittest.main()
