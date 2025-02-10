
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://saucedemo.com/')
    time.sleep(5)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    try:
        # Adding items to cart
        bike_light = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '2'

        # Reset cart
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        cart_count = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_count) == 0

        # Add bolt t-shirt after reset
        fleece_jacket.click()  # This is the locator for 'Bolt T-Shirt'
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '1'

        print('Test Passed')
        exit(0)

    except Exception as e:
        print(f'Test Failed: {e}')
        exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
