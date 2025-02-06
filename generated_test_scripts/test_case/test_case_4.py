
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.example.com")  # Replace with the actual URL

    def test_checkout_process(self):
        driver = self.driver
        login_page = LoginPage(driver)
        
        # Step 1: Log in
        login_page.login("valid_username", "valid_password")  # Replace with valid credentials
        
        # Step 2: Add 'Bike Light' and 'Fleece Jacket' to the cart
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket").click()
        
        # Validate items added to cart
        cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
        self.assertEqual(cart_badge.text, "2")
        
        # Step 3: Proceed to checkout
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        
        # Step 4: Enter the checkout information
        driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("somename")
        driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("lastname")
        driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
        
        # Step 5: Click 'Continue'
        driver.find_element(By.CSS_SELECTOR, "#continue").click()
        
        # Verification: 'Payment Information' label should be visible
        payment_info_label = driver.find_element(By.CSS_SELECTOR, "[data-test='payment-info-label']")
        self.assertTrue(payment_info_label.is_displayed(), "Payment Information label is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
