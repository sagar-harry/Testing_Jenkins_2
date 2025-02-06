
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class TestPurchaseFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.example.com/login') # Replace with actual URL

    def test_purchase_flow(self):
        driver = self.driver
        
        # Step 1: Log into the application
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        self.login(username, password, login_button)

        # Step 2: Add 'Bike Light' to the cart
        bike_light = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        bike_light.click()

        # Step 3: Add 'Fleece Jacket' to the cart
        fleece_jacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        fleece_jacket.click()

        # Step 4: Click on the cart icon
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        cart_icon.click()

        # Step 5: Proceed to checkout
        checkout = driver.find_element(By.ID, "checkout")
        checkout.click()

        # Step 6: Enter personal information
        first_name = driver.find_element(By.ID, "first-name")
        first_name.send_keys("somename")
        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("lastname")
        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("123456")

        # Step 7: Continue to complete the purchase
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        
        finish_button = driver.find_element(By.ID, "finish")
        finish_button.click()

        # Step 8: Return to the homepage
        back_to_products = driver.find_element(By.ID, "back-to-products")
        back_to_products.click()

        # Step 9: Log out
        burger_menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
        burger_menu_btn.click()
        
        logout_link = driver.find_element(By.ID, "logout_sidebar_link")
        logout_link.click()

    def login(self, username, password, login_button):
        username.send_keys("valid_username")  # Replace with actual credentials
        password.send_keys("valid_password")  # Replace with actual credentials
        login_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
