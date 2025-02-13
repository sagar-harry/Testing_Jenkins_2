
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def test_purchase_flow():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()
    
    try:
        # Login
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

        # Add items to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Proceed to checkout
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        # Enter shipping details
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Finish purchase
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        time.sleep(3)

        # Logout
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        time.sleep(3)

        driver.quit()
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

test_purchase_flow()
