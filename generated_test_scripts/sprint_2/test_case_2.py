
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = '//*[@id="user-name"]'
        self.password_input = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(3)

def test_cart_count():
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
  
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        bike_light_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        cart_badge = '//*[@id="shopping_cart_container"]/a/span'

        bike_light_button.click()
        time.sleep(3)
        fleece_jacket_button.click()
        time.sleep(3)

        cart_count = driver.find_element(By.XPATH, cart_badge).text
        if cart_count == '2':
            exit(0)
        else:
            exit(1)
    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)
    finally:
        driver.quit()

test_cart_count()
