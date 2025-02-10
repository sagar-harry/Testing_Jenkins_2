
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def login(self, driver, username, password):
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def run_test():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    login_page = LoginPage()
    login_page.login(driver, "standard_user", "secret_sauce")

    try:
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_button.click()
        time.sleep(3)

        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket_button.click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        cart_count = cart_badge.text
        time.sleep(3)

        assert cart_count == '2', f"Expected cart count '2', but got '{cart_count}'"
        
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
