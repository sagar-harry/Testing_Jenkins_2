
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    URL = "https://saucedemo.com/"
    USERNAME_INPUT = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(5)  # Wait for 5 seconds after opening the page
        self.driver.maximize_window()  # Maximize the page

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)
        time.sleep(3)  # Wait for 3 seconds before action
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)
        time.sleep(3)  # Wait for 3 seconds before action
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()
        time.sleep(3)


class CartTest:
    BIKE_LIGHT_BUTTON = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    FLEECE_JACKET_BUTTON = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    CART_COUNT = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    def __init__(self, driver):
        self.driver = driver

    def test_cart_count(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BIKE_LIGHT_BUTTON)
        ).click()
        time.sleep(3)  # Wait for 3 seconds before action
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FLEECE_JACKET_BUTTON)
        ).click()
        time.sleep(3)  # Wait for 3 seconds before action

        cart_count = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_COUNT)
        ).text
        time.sleep(3)  # Wait for 3 seconds before action

        if cart_count == '2':
            return 0
        else:
            return 1


if __name__ == "__main__":
    options = Options()
    # options.add_argument("--headless")  # Uncomment this line if you want to run the test headlessly
    driver = webdriver.Chrome(service=ChromeService(), options=options)
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        cart_test = CartTest(driver)
        result = cart_test.test_cart_count()

        print("Test Passed!" if result == 0 else "Test Failed!")
    finally:
        driver.quit()
