
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def main():
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Go to URL
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait 5 seconds
        driver.maximize_window()

        # Login
        login_page(driver)
        
        # Add items to cart
        time.sleep(3)
        add_to_cart(driver, "bike light")
        time.sleep(3)
        add_to_cart(driver, "fleece jacket")
        
        # Go to cart and proceed to checkout
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        
        # Enter user information
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        
        # Complete purchase
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        
        # Return to homepage
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        
        # Logout
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

        # Close driver
        driver.quit()
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

def login_page(driver):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def add_to_cart(driver, item_name):
    if item_name == "bike light":
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    elif item_name == "fleece jacket":
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

if __name__ == "__main__":
    main()
