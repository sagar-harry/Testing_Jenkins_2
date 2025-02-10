
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)
        
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        time.sleep(3)
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        
        time.sleep(3)
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket.click()
        
        time.sleep(3)
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))

        if cart_count.text == '2':
            exit_code = 0
        else:
            exit_code = 1

    except Exception as e:
        print(f"An exception occurred: {e}")
        exit_code = 1
        
    finally:
        driver.quit()
        exit(exit_code)

if __name__ == "__main__":
    main()
