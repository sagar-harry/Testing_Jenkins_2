
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_name_input = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        user_name_input.clear()
        user_name_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def main():
    try:
        url = "https://saucedemo.com/"
        username = "standard_user"
        password = "secret_sauce"

        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")

        # Initialize the webdriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)

        # Perform login
        login_page = LoginPage(driver)
        login_page.login(username, password)

        # Add 'Bike Light' to the cart
        bike_light_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        bike_light_button.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket_button.click()
        time.sleep(3)

        # Verify cart count
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert cart_count.text == "2", "Cart item count is incorrect"
        
        driver.quit()
        exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    main()
