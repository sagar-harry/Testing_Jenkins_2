
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Function to initialize the webdriver with specified configurations
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Function for the LoginPage class to handle login functionality
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://saucedemo.com/")
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

# Main test function to execute the test scenario
def test_ui():
    driver = init_driver()
    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add Bike Light to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        # Add Fleece Jacket to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart count is 2
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_count != '2':
            print("Test Failed: Cart count after adding items is not 2")
            driver.quit()
            exit(1)

        # Reset cart by removing both items
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
        for item in driver.find_elements(By.XPATH, "//button[contains(text(),'Remove')]"):
            item.click()
            time.sleep(3)

        # Verify cart is empty (cart count span should not be present)
        if driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'):
            print("Test Failed: Cart is not empty after reset")
            driver.quit()
            exit(1)

        # Add Bolt T-Shirt to the cart
        driver.back()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart count is 1
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        if cart_count != '1':
            print("Test Failed: Cart count after adding Bolt T-Shirt is not 1")
            driver.quit()
            exit(1)

        print("Test Passed")
        driver.quit()
        exit(0)

    except Exception as e:
        print(f"Exception occurred: {e}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    test_ui()
