
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    try:
        # Chrome options for headless, incognito, and disable notifications
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        
        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for the page to load
        
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

        # Proceed to cart and checkout
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        # Enter checkout information
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)
        
        # Continue to finish purchase
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)

        # Return to homepage
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))).click()
        
        # Logout
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
        
        # Exit with success code
        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        # Exit with failure code
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    run_test()
