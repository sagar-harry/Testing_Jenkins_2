
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Configure options for headless, incognito, disable notifications
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--start-maximized")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Login using LoginPage class method (assuming it's implemented correctly)
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
    )
    login_button.click()
    time.sleep(3)

    # Add 'Bike Light' to the cart
    bike_light = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    bike_light.click()
    time.sleep(3)

    # Add 'Fleece Jacket' to the cart
    fleece_jacket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    fleece_jacket.click()
    time.sleep(3)

    # Verify cart badge shows '2'
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    if cart_count.text == '2':
        print("Test Passed: Cart badge displays '2'")
        sys.exit(0)
    else:
        print("Test Failed: Cart badge does not display '2'")
        sys.exit(1)

except Exception as e:
    print(f"Test Failed: An exception occurred - {e}")
    sys.exit(1)
finally:
    driver.quit()
