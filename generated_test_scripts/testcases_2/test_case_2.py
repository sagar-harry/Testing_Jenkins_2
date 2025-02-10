
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
        self.username_input = "//*[@id='user-name']"
        self.password_input = "//*[@id='password']"
        self.login_button = "//*[@id='login-button']"

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.username_input))
        )
        username_field.send_keys(username)
        time.sleep(3)
        password_field = self.driver.find_element(By.XPATH, self.password_input)
        password_field.send_keys(password)
        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, self.login_button)
        login_button.click()

def test_ui_cart_count():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        time.sleep(3)

        bike_light_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        bike_light_button.click()
        time.sleep(3)

        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        )
        fleece_jacket_button.click()
        time.sleep(3)

        cart_count_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span"))
        )
        cart_count = cart_count_element.text
        assert cart_count == "2", f"Expected cart count to be '2', but got '{cart_count}'"

        print("Test case passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test case failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_ui_cart_count()
