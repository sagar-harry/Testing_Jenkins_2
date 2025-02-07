
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def setup_driver():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

def wait_and_act(driver, xpath):
    time.sleep(3)
    driver.find_element(By.XPATH, xpath).click()

def main():
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        wait_and_act(driver, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        wait_and_act(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        # Assert that cart badge shows '2'
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '2'

        # Reset cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        wait_and_act(driver, '//*[@id="remove-sauce-labs-bike-light"]')
        wait_and_act(driver, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')
        driver.get("https://www.saucedemo.com/") # Go back to home to refresh the cart

        # Add 'Bolt T-Shirt' to the cart after reset
        wait_and_act(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        # Assert that cart badge shows '1'
        cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_badge.text == '1'

        print("Test case passed")
        exit(0)

    except Exception as e:
        print("Test case failed:", str(e))
        exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
