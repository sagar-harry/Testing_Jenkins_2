
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
        self.username = '//*[@id="user-name"]'
        self.password = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.username))).send_keys(username)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.password))).send_keys(password)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.login_button))).click()
        time.sleep(3)

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    
    time.sleep(5) # Wait after opening the page

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    try:
        # Add Bike Light to the cart
        bike_light_xpath = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, bike_light_xpath))).click()
        time.sleep(3)
        
        # Add Fleece Jacket to the cart
        fleece_jacket_xpath = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, fleece_jacket_xpath))).click()
        time.sleep(3)
        
        # Check if the cart badge displays '2'
        cart_count_xpath = '//*[@id="shopping_cart_container"]/a/span'
        cart_count_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cart_count_xpath)))
        
        if cart_count_element.text == '2':
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)
            
    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
