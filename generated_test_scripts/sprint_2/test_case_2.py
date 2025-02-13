
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()

def run_test():
    # Configure Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    try:
        # Open the URL
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        # Log in using LoginPage class
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')
        time.sleep(3)
        
        # Add 'Bike Light' to cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket.click()
        time.sleep(3)
        
        # Verify cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '2', "Cart count is incorrect"
        
        # Exit with success code
        print("Test case passed")
        driver.quit()
        exit(0)
    except Exception as e:
        # Exit with failure code
        print("Test case failed:", str(e))
        driver.quit()
        exit(1)

if __name__ == "__main__":
    run_test()
