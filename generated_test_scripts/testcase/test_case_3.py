
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        user_input.send_keys(username)
        pwd_input = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        pwd_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

def run_test():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        # Initialize driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        driver.maximize_window()

        # Login
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')
        time.sleep(3)

        # Add 'Bike Light' to cart
        bike_light = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        fleece_jacket = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket.click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '2'
        time.sleep(3)

        # Reset the cart
        # Assuming there is now a way to reset (as it's not explicit in locators)
        fleece_jacket.click()  # Remove Fleece Jacket (if toggling add to remove)
        time.sleep(3)
        bike_light.click()  # Remove Bike Light (if toggling add to remove)
        time.sleep(3)

        # Verify cart is empty (cart badge should not be present)
        try:
            WebDriverWait(driver, 3).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        except:
            raised_exception = True
            cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
            assert cart_count.text == ""
            raised_exception = False

        # Add 'Bolt T-Shirt' after reset
        bolt_t_shirt = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        bolt_t_shirt.click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '1'

        driver.quit()
        exit(0)
        
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    run_test()
