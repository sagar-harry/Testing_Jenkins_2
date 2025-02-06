
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

class PurchaseFlowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://www.saucedemo.com")  # replace with actual URL of the application
        cls.login_page = LoginPage(cls.driver)

    def test_complete_purchase_flow(self):
        # Login
        self.login_page.login("valid_user", "valid_password")

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Go to cart
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()

        # Proceed to checkout
        self.driver.find_element(By.ID, "checkout").click()

        # Enter checkout information and continue
        self.driver.find_element(By.ID, "first-name").send_keys("somename")
        self.driver.find_element(By.ID, "last-name").send_keys("lastname")
        self.driver.find_element(By.ID, "postal-code").send_keys("123456")
        self.driver.find_element(By.ID, "continue").click()

        # Finish purchase
        self.driver.find_element(By.ID, "finish").click()

        # Validate return to homepage
        self.driver.find_element(By.ID, "back-to-products").click()
        self.assertTrue(self.driver.current_url.endswith('/inventory.html'))

        # Log out
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        self.assertTrue(self.driver.current_url.endswith('/'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
