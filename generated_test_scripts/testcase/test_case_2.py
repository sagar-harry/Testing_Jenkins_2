
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def test_add_items_to_cart():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.example.com')  # replace with actual URL
    driver.maximize_window()
    time.sleep(5)

    login_page = LoginPage(driver)
    login_page.login('test_user', 'test_password')

    try:
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        cart_count_element = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        cart_count = cart_count_element.text

        assert cart_count == '2', "Cart count is incorrect"

        print("Test passed.")
        exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_add_items_to_cart()
