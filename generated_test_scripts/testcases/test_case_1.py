
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_purchase_flow():
    try:
        options = Options()
        options.headless = True
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        
        time.sleep(5)
        driver.maximize_window()
        
        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        time.sleep(3)
        
        # Add items to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        
        # Checkout
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        
        # Logout
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        
        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        print(str(e))
        driver.quit()
        sys.exit(1)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        
        time.sleep(3)

if __name__ == "__main__":
    test_purchase_flow()
