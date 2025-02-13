
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

# Set up Chrome options for headless mode, incognito, and disabling notifications
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument('--incognito')
options.add_argument('--window-size=1920x1080')

# Initialize the driver
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the website
    driver.get('https://saucedemo.com/')
    time.sleep(5)
    
    # Maximize window
    driver.maximize_window()
    
    # Log in using the LoginPage class method
    class LoginPage:
        @staticmethod
        def login(driver, username, password):
            username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
            password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
            login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

            username_field.send_keys(username)
            time.sleep(3)
            password_field.send_keys(password)
            time.sleep(3)
            login_button.click()
            time.sleep(3)
    
    LoginPage.login(driver, 'standard_user', 'secret_sauce')

    # Add 'Bike Light' to the cart
    bike_light_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    bike_light_button.click()
    time.sleep(3)

    # Add 'Fleece Jacket' to the cart
    fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    fleece_jacket_button.click()
    time.sleep(3)

    # Verify the cart count
    cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_count.text == '2', "Cart count is incorrect"

    # Exit code 0 if test passed
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    # Exit code 1 if test failed
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
