
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(3)
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
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        time.sleep(3)
        bike_light.click()
        time.sleep(3)

        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        time.sleep(3)
        cart_icon.click()
        time.sleep(3)

        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        time.sleep(3)
        checkout_button.click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

        first_name.send_keys("somename")
        time.sleep(3)
        last_name.send_keys("lastname")
        time.sleep(3)
        zip_code.send_keys("123456")
        time.sleep(3)

        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        time.sleep(3)
        continue_button.click()
        time.sleep(3)

        payment_information = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')

        if payment_information.is_displayed():
            print("Test Passed: 'Payment Information' label is visible.")
            sys.exit(0)
        else:
            print("Test Failed: 'Payment Information' label is not visible.")
            sys.exit(1)
    except Exception as e:
        print(f"Test Failed with Exception: {e}")
        sys.exit(1)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
