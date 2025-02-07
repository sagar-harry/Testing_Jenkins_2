
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = '//*[@id="user-name"]'
        self.password_locator = '//*[@id="password"]'
        self.login_button_locator = '//*[@id="login-button"]'

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_locator).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button_locator).click()
        time.sleep(3)

def test_add_items_to_cart():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        bike_light_locator = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
        fleece_jacket_locator = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        cart_count_locator = '//*[@id="shopping_cart_container"]/a/span'

        driver.find_element(By.XPATH, bike_light_locator).click()
        time.sleep(3)
        driver.find_element(By.XPATH, fleece_jacket_locator).click()
        time.sleep(3)
        
        cart_count_element = driver.find_element(By.XPATH, cart_count_locator)
        time.sleep(3)
        cart_count = cart_count_element.text

        assert cart_count == '2', "The cart count did not match the expected value."
        
        print("Test passed")
        exit(0)

    except Exception as e:
        print(f"Test failed: {str(e)}")
        exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_add_items_to_cart()
