
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

class TestCart:
    def __init__(self, driver):
        self.driver = driver
    
    def wait_and_find_element(self, by_type, value):
        time.sleep(3)
        return self.driver.find_element(by_type, value)

    def test_cart_functionality(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.login("standard_user", "secret_sauce")
            time.sleep(5)
            
            # Add 'Bike Light' to the cart
            bike_light_button = self.wait_and_find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
            bike_light_button.click()
            
            # Add 'Fleece Jacket' to the cart
            fleece_jacket_button = self.wait_and_find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
            fleece_jacket_button.click()

            # Assert cart badge is '2'
            cart_badge = self.wait_and_find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert cart_badge.text == '2', "Cart badge should display '2'"

            # Reset the cart
            self.driver.find_element(By.XPATH, '//*[@data-test="remove-sauce-labs-bike-light"]').click()
            self.driver.find_element(By.XPATH, '//*[@data-test="remove-sauce-labs-bolt-t-shirt"]').click()

            # Check if cart is empty by asserting absence of cart badge
            cart_badge_elements = self.driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert len(cart_badge_elements) == 0, "Cart badge should be absent"

            # Add 'Bolt T-Shirt' to the cart after reset
            bolt_t_shirt_button = self.wait_and_find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
            bolt_t_shirt_button.click()

            # Assert cart badge is '1'
            cart_badge = self.wait_and_find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert cart_badge.text == '1', "Cart badge should display '1'"
            
            sys.exit(0)

        except AssertionError as e:
            print(f"Assertion Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
            
if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    
    time.sleep(5)
    
    test_cart = TestCart(driver)
    test_cart.test_cart_functionality()
    
    driver.quit()
