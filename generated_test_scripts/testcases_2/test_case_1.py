
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

def test_purchase_flow():
    try:
        driver = setup_driver()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # Login
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        time.sleep(3)

        # Add items to cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        ).click()
        time.sleep(3)

        # Go to cart and checkout
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a"))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='checkout']"))
        ).click()
        time.sleep(3)

        # Enter checkout information and continue
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='first-name']"))
        ).send_keys("somename")
        time.sleep(3)

        driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("lastname")
        time.sleep(3)

        driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("123456")
        time.sleep(3)

        driver.find_element(By.XPATH, "//*[@id='continue']").click()
        time.sleep(3)
        
        # Complete purchase
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='finish']"))
        ).click()
        time.sleep(3)
        
        # Return to homepage
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='back-to-products']"))
        ).click()
        time.sleep(3)
        
        # Logout
        driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='logout_sidebar_link']"))
        ).click()
        time.sleep(3)
        
        driver.quit()
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

test_purchase_flow()
