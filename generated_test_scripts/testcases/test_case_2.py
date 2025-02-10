
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light_button.click()
        time.sleep(3)

        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket_button.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        
        if cart_count.text == '2':
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
