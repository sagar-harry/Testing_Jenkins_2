
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        username_field.send_keys(username)
        time.sleep(3)
        
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        password_field.send_keys(password)
        time.sleep(3)
        
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()
        time.sleep(3)

def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()
    return driver

def test_scenario():
    try:
        driver = open_browser()
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        add_bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        add_bike_light.click()
        time.sleep(3)

        add_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        add_fleece_jacket.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2', "Test Failed: Cart count should be '2'"

        reset_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        reset_cart.click()
        time.sleep(3)

        cart_empty = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_empty.text == '', "Test Failed: Cart should be empty"

        add_bolt_tshirt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        add_bolt_tshirt.click()
        time.sleep(3)

        cart_count_after_reset = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count_after_reset.text == '1', "Test Failed: Cart count should be '1'"

        print("All test scenarios passed successfully.")
        return 0

    except Exception as e:
        print(f"Test failed due to: {e}")
        return 1

    finally:
        driver.quit()

if __name__ == "__main__":
    test_result = test_scenario()
