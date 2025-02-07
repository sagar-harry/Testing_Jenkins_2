
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def login(self, driver, username, password):
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def execute_test():
    try:
        # Setup Chrome options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        
        # Initialize the WebDriver
        driver = webdriver.Chrome(options=options)
        
        # Open login page
        driver.get('https://example.com/login')
        time.sleep(5)  # wait after opening page
        driver.maximize_window()
        
        login_page = LoginPage()
        
        # Perform login
        time.sleep(3)
        login_page.login(driver, 'valid_username', 'valid_password')
        
        # Add items to cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)
        
        # Proceed to cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        ).click()
        time.sleep(3)
        
        # Checkout process
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        ).click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))
        ).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]'))
        ).click()
        time.sleep(3)
        
        # Return to homepage
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))
        ).click()
        time.sleep(3)
        
        # Log out
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))
        ).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))
        ).click()
        time.sleep(3)
        
        print("Test Case Passed")
        driver.quit()
        exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    execute_test()
