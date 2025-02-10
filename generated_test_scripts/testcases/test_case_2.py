
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Helper function to perform login
def login(username, password):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

try:
    # Open website
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Perform login
    login("standard_user", "secret_sauce")

    # Wait for bike light element and add to cart
    bike_light = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    time.sleep(3)
    bike_light.click()

    # Wait for fleece jacket element and add to cart
    fleece_jacket = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    time.sleep(3)
    fleece_jacket.click()

    # Verify cart badge count
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    time.sleep(3)

    if cart_count.text == '2':
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
