
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(3)
        username_input = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_input.send_keys(username)
        time.sleep(3)
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()

def main():
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()
        
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        time.sleep(3)
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()

        time.sleep(3)
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '2', "Cart count is not correct after adding two items."

        # Resetting the cart by removing items
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()

        time.sleep(3)
        try:
            cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert cart_count.text == '', "Cart is not empty after reset."
        except:
            pass

        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == '1', "Cart count is not correct after adding one item post reset."

        driver.quit()
        exit(0)
    except Exception as e:
        print("Test case failed due to: ", str(e))
        if driver:
            driver.quit()
        exit(1)

if __name__ == "__main__":
    main()
