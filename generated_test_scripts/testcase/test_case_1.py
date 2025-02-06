
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = '//*[@id="user-name"]'
        self.password_field = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'
    
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.username_field))).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(3)

def run_test():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.yourwebsite.com/login")
    
    try:
        login_page = LoginPage(driver)
        login_page.login("valid_username", "valid_password")
        
        # Add products to the cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Go to cart and checkout
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)
        
        # Enter user details
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)
        
        # Continue and finish purchase
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)
        
        # Return to home page
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        time.sleep(3)
        
        # Logout
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        time.sleep(3)
        
        print("Test Passed")
        return 0

    except Exception as e:
        print(f"Test Failed: {e}")
        return 1

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
