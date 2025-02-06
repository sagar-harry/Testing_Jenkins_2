
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        user_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

def run_test_case():
    options = Options()
    options.headless = True
    options.add_argument('--incognito')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        bike_light = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        fleece_jacket = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        assert cart_count.text == "2", "Cart badge count should be '2'"

        reset_cart_button = driver.find_element(By.XPATH, '//*[@id="reset-sauce-labs-bike-light"]')
        reset_cart_button.click()
        time.sleep(3)
        reset_cart_button = driver.find_element(By.XPATH, '//*[@id="reset-sauce-labs-bolt-t-shirt"]')
        reset_cart_button.click()
        time.sleep(3)

        assert not cart_count.is_displayed(), "Cart should be empty"

        bolt_tshirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bolt_tshirt.click()
        time.sleep(3)

        assert cart_count.text == "1", "Cart badge count should be '1'"

        driver.quit()
        exit(0)
    except Exception as e:
        print(e)
        driver.quit()
        exit(1)

if __name__ == "__main__":
    run_test_case()
