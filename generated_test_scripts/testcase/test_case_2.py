
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

class TestCartFunctionality:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_add_items_to_cart(self):
        # Given the user is logged in
        self.login_page.login("standard_user", "secret_sauce")
        
        # When they add 'Bike Light' and 'Fleece Jacket' to the cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Then the cart badge should display '2'
        cart_count = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '2', f"Expected cart count to be '2', but got '{cart_count}'"

if __name__ == "__main__":
    test = TestCartFunctionality()
    test.setup_method()
    test.test_add_items_to_cart()
    test.teardown_method()
