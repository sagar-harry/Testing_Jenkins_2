
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class UITestScenario(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com")  # Replace with the actual URL

    def test_add_items_to_cart_and_verify_count(self):
        login_page = LoginPage(self.driver)
        login_page.login("test_user", "test_password")  # Replace with actual test creds

        # Add items to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Verify cart count
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "2", "Cart badge should display '2'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
