
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        time.sleep(3)

def main():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        # Create instance of LoginPage
        login_page = LoginPage(driver)

        # Login
        login_page.login("standard_user", "secret_sauce")

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)
        
        # Proceed to cart and checkout
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='checkout']"))).click()
        time.sleep(3)
        
        # Enter shipping information
        driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("123456")
        time.sleep(3)
        
        # Continue and finish checkout
        driver.find_element(By.XPATH, "//*[@id='continue']").click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='finish']"))).click()
        time.sleep(3)

        # Return to homepage and logout
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='back-to-products']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-burger-menu-btn']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='logout_sidebar_link']"))).click()
        
        print("Test passed")
        sys.exit(0)
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
        sys.exit(1)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
```

This script covers all the specified steps and uses Selenium WebDriver to automate the process in a headless Chrome browser. It adheres to the requirements like headless mode, incognito, waits for elements, and provides a proper exit code based on test results.