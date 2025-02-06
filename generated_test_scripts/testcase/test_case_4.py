
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import sys

def run_test():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    
    # Initialize the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for page to load
        
        # Maximize browser window
        driver.maximize_window()
        
        # Login Page object class
        class LoginPage:
            USERNAME_INPUT = (By.XPATH, '//*[@id="user-name"]')
            PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
            LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
            
            @staticmethod
            def login(driver):
                driver.find_element(*LoginPage.USERNAME_INPUT).send_keys("standard_user")
                time.sleep(3)
                driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys("secret_sauce")
                time.sleep(3)
                driver.find_element(*LoginPage.LOGIN_BUTTON).click()
                time.sleep(3)
        
        # Log in
        LoginPage.login(driver)
        
        # Add Bike Light to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        # Add Fleece Jacket to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Open Cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        
        # Proceed to Checkout
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)
        
        # Enter Checkout Information
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)
        
        # Continue to Payment
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)
        
        # Verify Payment Information label is visible
        payment_information = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        
        if payment_information.is_displayed():
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)
            
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    
    finally:
        driver.quit()

run_test()
