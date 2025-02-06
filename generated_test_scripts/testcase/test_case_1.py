
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    URL = "https://saucedemo.com/"
    USERNAME_LOCATOR = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_LOCATOR = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[@id="login-button"]')

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get(self.URL)
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME_LOCATOR)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_LOCATOR)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON_LOCATOR)).click()


def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    
    service = Service('/path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys('somename')
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys('lastname')
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys('123456')
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]')))
        
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()

        print("Test case passed.")
        sys.exit(0)
        
    except Exception as e:
        print(f"Test case failed: {e}")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
