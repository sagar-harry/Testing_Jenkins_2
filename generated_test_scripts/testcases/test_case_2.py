
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_field.clear()
        username_field.send_keys(username)
        time.sleep(3)
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def test_add_items_to_cart():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the website and maximize window
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        # Log in using the LoginPage class
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add 'Bike Light' to the cart
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light_button.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket_button.click()
        time.sleep(3)

        # Verify cart count
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )

        assert cart_count.text == '2', "Cart badge does not display '2'."
        
        # If the test passes
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {str(e)}")
        # If the test fails
        sys.exit(1)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_add_items_to_cart()
