
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Setup Chrome options
options = Options()
options.headless = True
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")
options.add_argument("--window-size=1920,1080")

# Initialize the web driver
driver = webdriver.Chrome(options=options)

try:
    # Open the website
    driver.get('https://saucedemo.com/')
    time.sleep(5)
    driver.maximize_window()

    # Login using the LoginPage class
    class LoginPage:
        def __init__(self, driver):
            self.driver = driver

        def login(self, username, password):
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
            time.sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    # Add 'Bike Light' to the cart
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Add 'Fleece Jacket' to the cart
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Verify cart badge displays '2'
    cart_count = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))).text
    assert cart_count == '2', f"Cart count should be '2', but got '{cart_count}'"

    print("Test passed")
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
