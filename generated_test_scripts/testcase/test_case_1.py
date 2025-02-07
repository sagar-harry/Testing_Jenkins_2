
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        usr_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        usr_field.send_keys(username)
        time.sleep(3)

        pwd_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        pwd_field.send_keys(password)
        time.sleep(3)

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_btn.click()
        time.sleep(3)

def test_purchase_flow():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.example.com/login")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("valid_username", "valid_password")

        wait = WebDriverWait(driver, 10)
        
        bike_light = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        time.sleep(3)
        
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)
        
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)
        
        checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout.click()
        time.sleep(3)
        
        first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        first_name.send_keys('somename')
        time.sleep(3)
        
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        last_name.send_keys('lastname')
        time.sleep(3)
        
        postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        postal_code.send_keys('123456')
        time.sleep(3)
        
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)
        
        finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
        finish_button.click()
        time.sleep(3)
        
        back_to_products = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
        back_to_products.click()
        time.sleep(3)

        logout_sidebar = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        logout_sidebar.click()
        time.sleep(3)
        
        logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
        logout_button.click()
        time.sleep(3)

        print("Test Passed")
        exit(0)
    
    except TimeoutException:
        print("Test Failed: Timeout occurred")
        exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_purchase_flow()
