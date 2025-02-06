
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
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Add Bike Light to cart
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light_button.click()
        time.sleep(3)

        # Add Fleece Jacket to cart
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket_button.click()
        time.sleep(3)

        # Verify cart count
        cart_count_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        cart_count = cart_count_element.text

        assert cart_count == '2', "Cart count does not match expected value"

        driver.quit()
        sys.exit(0)

    except AssertionError as e:
        print(f"Test Failed: {str(e)}")
        driver.quit()
        sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    run_test()
