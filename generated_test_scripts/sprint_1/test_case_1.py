
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Configurations for headless mode and browser options
options = Options()
options.headless = True
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")

# Initialize the driver
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

try:
    # Step 1: Open the website
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    # Step 2: Login
    class LoginPage:
        @staticmethod
        def login(username, password):
            driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            time.sleep(3)

    LoginPage.login("standard_user", "secret_sauce")

    # Step 3: Add Bike Light and Fleece Jacket to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Check the cart badge
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    if cart_count.text != "2":
        raise AssertionError("Cart badge did not display '2' after adding items")

    # Step 4: Reset the cart
    # (Assuming there is a "Reset" or "Remove" option logic here to clear the cart)

    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    time.sleep(3)
    driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
    time.sleep(3)

    # Check cart badge is empty
    try:
        cart_count = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
    except:
        raise AssertionError("Cart is not empty after reset")

    # Step 5: Add Bolt T-Shirt to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Check the cart badge
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    if cart_count.text != "1":
        raise AssertionError("Cart badge did not display '1' after adding Bolt T-Shirt")

    sys.exit(0)  # Test case passed

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)  # Test case failed

finally:
    driver.quit()
