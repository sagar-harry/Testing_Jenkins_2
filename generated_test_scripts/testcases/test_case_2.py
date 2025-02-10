
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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def test_add_to_cart():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '2'
        
        driver.quit()
        exit(0)  # Test case passed
    except Exception as e:
        driver.quit()
        exit(1)  # Test case failed

if __name__ == '__main__':
    test_add_to_cart()
