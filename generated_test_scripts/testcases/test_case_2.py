
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        username_field.send_keys(username)
        time.sleep(3)

        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        password_field.send_keys(password)
        time.sleep(3)

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        login_button.click()
        time.sleep(3)

def test_cart_count():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-notifications')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://saucedemo.com/')
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        bike_light_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_button.click()
        time.sleep(3)

        fleece_jacket_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket_button.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        if cart_count.text == '2':
            driver.quit()
            sys.exit(0)

        driver.quit()
        sys.exit(1)

    except Exception as e:
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_cart_count()
