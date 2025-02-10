
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
        self.username_locator = '//*[@id="user-name"]'
        self.password_locator = '//*[@id="password"]'
        self.login_button_locator = '//*[@id="login-button"]'

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_locator).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button_locator).click()
        time.sleep(3)

def test_cart_operations():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light_locator = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        fleece_jacket_locator = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        cart_count_locator = '//*[@id="shopping_cart_container"]/a/span'

        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, bike_light_locator))).click()
        time.sleep(3)
        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, fleece_jacket_locator))).click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, cart_count_locator))).text
        assert cart_count == '2', f"Cart count expected '2', but got '{cart_count}'"
        
        # Reset the cart
        driver.find_element(By.XPATH, '//*[contains(text(),"Remove")]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[contains(text(),"Remove")]').click()
        time.sleep(3)

        # Verify the cart is empty
        try:
            cart_count = driver.find_element(By.XPATH, cart_count_locator).text
        except:
            cart_count = '0'  # No badge means empty

        assert cart_count == '0', f"Cart count expected '0', but got '{cart_count}'"

        # Add 'Bolt T-Shirt' to the cart after reset
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, fleece_jacket_locator))).click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, cart_count_locator))).text
        assert cart_count == '1', f"Cart count expected '1', but got '{cart_count}'"

        sys.exit(0)

    except Exception as e:
        print("Test failed:", str(e))
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_cart_operations()
