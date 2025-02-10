
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

def main():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")

    try:
        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        # Initialize LoginPage and login
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '2', 'Cart count should be 2'

        # Reset cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)

        # Add 'Bolt T-Shirt' after reset
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '1', 'Cart count should be 1'

        driver.quit()
        exit(0)
    except Exception as e:
        print("An error occurred:", e)
        driver.quit()
        exit(1)

if __name__ == "__main__":
    main()
