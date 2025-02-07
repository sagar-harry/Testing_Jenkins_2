
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    try:
        # Set up Chrome options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=options)
        
        # Open the application URL
        driver.get("YOUR_WEB_APP_URL")
        time.sleep(5)
        
        # Maximize the browser window
        driver.maximize_window()
        
        # Perform Login
        login_page = LoginPage(driver)
        login_page.login("your_username", "your_password")
        time.sleep(3)
        
        # Add 'Bike Light' to cart
        bike_light_el = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light_el.click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to cart
        fleece_jacket_el = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket_el.click()
        time.sleep(3)
        
        # Verify cart count
        cart_count_el = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        if cart_count_el.text != '2':
            sys.exit(1)
        
        # Reset the cart
        # Assuming there are buttons or options to reset the cart
        # Replace with actual selectors and actions
        # reset_cart_button = driver.find_element(By.XPATH, 'path_to_reset_button')
        # reset_cart_button.click()
        # Alternatively remove items manually
        bike_light_el = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        bike_light_el.click()
        fleece_jacket_el.click()
        time.sleep(3)
        
        # Verify cart is empty
        cart_count_text = cart_count_el.text if cart_count_el.is_displayed() else ''
        if cart_count_text:
            sys.exit(1)
        
        # Add 'Bolt T-Shirt' to cart
        bolt_tshirt_el = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bolt_tshirt_el.click()
        time.sleep(3)
        
        # Verify cart count
        if cart_count_el.text != '1':
            sys.exit(1)
        
        # Test case passed
        sys.exit(0)
        
    except Exception as e:
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
