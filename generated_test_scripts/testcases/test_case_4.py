
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
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def test_checkout_flow():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://saucedemo.com/')
    time.sleep(5)

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    try:
        # Add Bike Light to Cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        # Add Fleece Jacket to Cart
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)

        # Click on Cart Icon
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)

        # Proceed to Checkout
        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout_button.click()
        time.sleep(3)

        # Enter Checkout Information
        first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

        first_name_field.send_keys('somename')
        time.sleep(3)
        last_name_field.send_keys('lastname')
        time.sleep(3)
        zip_code_field.send_keys('123456')
        time.sleep(3)

        # Click Continue
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)

        # Verify Payment Information Label
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        if payment_info_label.is_displayed():
            driver.quit()
            sys.exit(0)
    except Exception as e:
        driver.quit()
        sys.exit(1)

if __name__ == '__main__':
    test_checkout_flow()
