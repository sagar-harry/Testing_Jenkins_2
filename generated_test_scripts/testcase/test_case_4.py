
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, '//*[@id="user-name"]')
        self.password_field = (By.XPATH, '//*[@id="password"]')
        self.login_button = (By.XPATH, '//*[@id="login-button"]')

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()


def test_checkout_payment_information():
    # Configure Chrome options
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)

        # Login
        login_page.login('standard_user', 'secret_sauce')
        time.sleep(3)

        # Add items to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()
        time.sleep(3)

        # Proceed to checkout
        cart_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        )
        cart_icon.click()
        time.sleep(3)

        checkout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        )
        checkout_button.click()
        time.sleep(3)

        # Enter checkout information
        first_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        first_name_field.send_keys('somename')
        time.sleep(3)

        last_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))
        )
        last_name_field.send_keys('lastname')
        time.sleep(3)

        zip_code_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))
        )
        zip_code_field.send_keys('123456')
        time.sleep(3)

        continue_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))
        )
        continue_button.click()
        time.sleep(3)

        # Assert the Payment Information label is visible
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )
        if payment_info_label.is_displayed():
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        print(f"Test failed due to: {e}")
        sys.exit(1)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_checkout_payment_information()
