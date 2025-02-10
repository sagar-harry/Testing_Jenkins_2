
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def wait_and_find(by, locator):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, locator)))

try:
    # Selenium options setup
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    # Login
    username_field = wait_and_find(By.XPATH, "//*[@id='user-name']")
    password_field = wait_and_find(By.XPATH, "//*[@id='password']")
    login_button = wait_and_find(By.XPATH, "//*[@id='login-button']")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    time.sleep(3)
    
    # Add items to cart
    wait_and_find(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(3)
    wait_and_find(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    time.sleep(3)

    # Proceed to checkout
    wait_and_find(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
    time.sleep(3)
    wait_and_find(By.XPATH, "//*[@id='checkout']").click()
    time.sleep(3)

    # Enter checkout information
    wait_and_find(By.XPATH, "//*[@id='first-name']").send_keys("somename")
    wait_and_find(By.XPATH, "//*[@id='last-name']").send_keys("lastname")
    wait_and_find(By.XPATH, "//*[@id='postal-code']").send_keys("123456")
    time.sleep(3)
    wait_and_find(By.XPATH, "//*[@id='continue']").click()
    time.sleep(3)

    # Complete the purchase
    wait_and_find(By.XPATH, "//*[@id='finish']").click()
    time.sleep(3)

    # Return to homepage
    wait_and_find(By.XPATH, "//*[@id='back-to-products']").click()
    time.sleep(3)

    # Logout
    wait_and_find(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
    time.sleep(3)
    wait_and_find(By.XPATH, "//*[@id='logout_sidebar_link']").click()
    
    # Test passed
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    # Test failed
    sys.exit(1)

finally:
    driver.quit()
