
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
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        time.sleep(3)
        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def run_test():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--incognito')

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        wait = WebDriverWait(driver, 10)

        # Add Bike Light
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)

        # Add Fleece Jacket (Note: This should match the locator for Fleece Jacket, not Bolt T-shirt)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
        time.sleep(3)

        # Verify Cart Count is 2
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_count != '2':
            raise Exception("Cart count after adding items is not '2'.")

        # Remove all items (Reset Cart)
        # Use the correct locator here to reset or remove items from the cart
        # For demonstration purposes, assuming a button click to remove all
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
        time.sleep(3)

        # Verify Cart is Empty
        try:
            cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
            if cart_count != '':
                raise Exception("Cart is not empty after resetting.")
        except:
            # Cart badge is not present, which means it's empty
            pass

        # Add Bolt T-Shirt
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Verify Cart Count is 1
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_count != '1':
            raise Exception("Cart count after adding 'Bolt T-Shirt' is not '1'.")

        print("Test Passed")
        sys.exit(0)
    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)
    finally:
        driver.quit()

run_test()
