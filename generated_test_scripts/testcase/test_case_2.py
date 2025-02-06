
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = '//*[@id="user-name"]'
        self.password_locator = '//*[@id="password"]'
        self.login_button_locator = '//*[@id="login-button"]'

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.username_locator))
        )
        username_field.send_keys(username)
        
        password_field = self.driver.find_element(By.XPATH, self.password_locator)
        password_field.send_keys(password)
        
        self.driver.find_element(By.XPATH, self.login_button_locator).click()

def test_add_to_cart():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get("https://example.com")  # Replace with actual URL
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        bike_light_locator = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        fleece_jacket_locator = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        cart_count_locator = '//*[@id="shopping_cart_container"]/a/span'

        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, bike_light_locator))
        )
        bike_light.click()
        time.sleep(3)

        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, fleece_jacket_locator))
        )
        fleece_jacket.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, cart_count_locator))
        )
        
        # Assert cart count
        if cart_count.text == '2':
            print("Test Passed")
            return 0
        else:
            print("Test Failed")
            return 1

    except Exception as e:
        print(f"Test Failed: {e}")
        return 1
    finally:
        driver.quit()

if __name__ == "__main__":
    result = test_add_to_cart()
    print("Exit status:", result)
