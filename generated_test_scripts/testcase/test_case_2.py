
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
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_input.send_keys(username)
        time.sleep(3)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_input.send_keys(password)
        time.sleep(3)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()
        time.sleep(3)

def main():
    url = 'https://saucedemo.com/'
    username = 'standard_user'
    password = 'secret_sauce'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)

    login_page = LoginPage(driver)
    login_page.login(username, password)

    bike_light_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    )
    bike_light_button.click()
    time.sleep(3)

    fleece_jacket_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    fleece_jacket_button.click()
    time.sleep(3)

    cart_count_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    cart_count = cart_count_element.text

    driver.quit()

    if cart_count == '2':
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
