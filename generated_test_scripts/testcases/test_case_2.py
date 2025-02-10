
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_cart_count():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        time.sleep(3)
        login_page.login()

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        cart_count_element = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        cart_count = cart_count_element.text
        
        assert cart_count == '2', f"Expected cart count '2', but got '{cart_count}'"
        
        exit(0)  # Exit with code 0 if test passed

    except Exception as e:
        print(str(e))
        exit(1)  # Exit with code 1 if test failed

    finally:
        driver.quit()

test_cart_count()
