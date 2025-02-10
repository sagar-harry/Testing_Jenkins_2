
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def wait_for_element(driver, by, locator):
    for _ in range(10):
        try:
            element = driver.find_element(by, locator)
            return element
        except:
            time.sleep(1)
    raise Exception("Element not found")

try:
    driver = setup_driver()
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    bike_light = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    time.sleep(3)
    bike_light.click()

    fleece_jacket = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    time.sleep(3)
    fleece_jacket.click()

    cart_count = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_count.text == '2'

    bike_light.click()
    time.sleep(3)
    fleece_jacket.click()
    time.sleep(3)

    cart_count = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert not cart_count.is_displayed()

    fleece_jacket.click()
    time.sleep(3)

    cart_count = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_count.text == '1'

    driver.quit()
    exit(0)

except Exception as e:
    print(f"Test case failed: {e}")
    driver.quit()
    exit(1)
