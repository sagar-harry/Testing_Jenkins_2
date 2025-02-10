
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)

    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Login
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add items to cart
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Open cart and proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    # Enter checkout information
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
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
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
    time.sleep(3)
    sys.exit(0)
except Exception as e:
    print(f"Error in test execution: {e}")
    sys.exit(1)
finally:
    driver.quit()
