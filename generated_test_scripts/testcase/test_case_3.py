
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
        
        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def run_test():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    
    driver = webdriver.Chrome(options=options)
    driver.get('https://example.com/')
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    try:
        # Add 'Bike Light' to cart
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light_button.click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to cart
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket_button.click()
        time.sleep(3)

        # Verify cart count is '2'
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2', "Cart count is not 2"
        time.sleep(3)
        
        # Reset cart (manual removal in this case)
        bike_light_button.click()
        time.sleep(3)
        fleece_jacket_button.click()
        time.sleep(3)

        cart_count = driver.execute_script(
            "return document.querySelector('#shopping_cart_container a span') ? document.querySelector('#shopping_cart_container a span').textContent : '0'"
        )
        assert cart_count == '0', "Cart is not empty after reset"

        # Add 'Bolt T-Shirt' to cart
        bolt_tshirt_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        bolt_tshirt_button.click()
        time.sleep(3)

        # Verify cart count is '1'
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '1', "Cart count is not 1"

        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

run_test()
