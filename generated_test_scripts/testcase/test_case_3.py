
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
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def run_test_case():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        # Add Bike Light and Fleece Jacket to cart
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '2'

        # Reset the cart (remove the added products)
        bike_light_remove = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        fleece_jacket_remove = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')

        bike_light_remove.click()
        time.sleep(3)
        fleece_jacket_remove.click()
        time.sleep(3)

        cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart.click()
        time.sleep(3)

        cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
        assert len(cart_items) == 0

        # Add Bolt T-Shirt to the cart after reset
        bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bolt_tshirt.click()
        time.sleep(3)

        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '1'

        driver.quit()
        exit(0)

    except AssertionError:
        driver.quit()
        exit(1)

run_test_case()
