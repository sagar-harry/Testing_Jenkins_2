
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def test_add_items_to_cart():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920x1080")

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Open URL
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # Maximize the window
        driver.maximize_window()

        # Perform login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Wait and add 'Bike Light' to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        time.sleep(3)
        bike_light.click()

        # Wait and add 'Fleece Jacket' to the cart
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        time.sleep(3)
        fleece_jacket.click()

        # Wait for the cart badge to display and check its value
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        time.sleep(3)
        assert cart_count.text == '2', "Cart count is not correct."

        # Pass the test
        print("Test Passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        # Clean up and close the driver
        driver.quit()

# Run the test
test_add_items_to_cart()
