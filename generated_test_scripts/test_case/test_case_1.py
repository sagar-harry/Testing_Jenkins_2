
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Page Objects
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class PurchaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")
        self.login_page = LoginPage(self.driver)

    def test_complete_purchase_flow(self):
        # Logging in
        self.login_page.login("standard_user", "secret_sauce")
        
        # Add Bike Light to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Add Fleece Jacket to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Click on Cart icon
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()

        # Proceed to checkout
        self.driver.find_element(By.ID, "checkout").click()

        # Enter Checkout Information
        self.driver.find_element(By.ID, "first-name").send_keys("somename")
        self.driver.find_element(By.ID, "last-name").send_keys("lastname")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()

        # Finish Purchase
        self.driver.find_element(By.ID, "finish").click()

        # Return to Home Page
        self.driver.find_element(By.ID, "back-to-products").click()

        # Logout
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()

        # Adding assertions for validation
        self.assertTrue(self.driver.find_element(By.ID, "login-button").is_displayed(), "Login button is not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
