
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)  # Wait for login to complete

class UITests:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_items_to_cart(self):
        self.setUp()
        self.login_page.login("standard_user", "secret_sauce")

        # Add Bike Light to the cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        # Add Fleece Jacket to the cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge shows '2'
        cart_count = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '2', f"Expected cart count to be '2', but got '{cart_count}'"

        # Reset the cart by removing items
        # Example assumes there is a 'remove' button with known locators for simplicity
        self.driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart is empty (No badge)
        cart_badge_elements = self.driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_badge_elements) == 0, "Expected cart badge to be empty"

        # Add Bolt T-Shirt to the cart after reset
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge shows '1'
        cart_count = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '1', f"Expected cart count to be '1', but got '{cart_count}'"

        self.tearDown()

if __name__ == "__main__":
    test = UITests()
    test.test_add_items_to_cart()
