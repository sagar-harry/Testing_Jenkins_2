
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_shopping_cart():
    # Setup Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=options)

    try:
        # Open the website
        driver.get('https://saucedemo.com/')
        time.sleep(5)  # Wait for 5 secs after opening the page
        driver.maximize_window()

        # Login to the website
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')
        time.sleep(3)  # Wait for 3 secs before next action

        # Add 'Bike Light' to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to the cart
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '2'

        # Reset the cart (remove the added products)
        # Assuming there's an easy reset feature or manual product removal required
        if cart_count.text == '2':
            # Logic to reset cart will be here (depends on website functionality)
            pass
        time.sleep(3)

        # Verify cart is empty
        assert cart_count.text == '0'

        # Add 'Bolt T-Shirt' to the cart
        # Adjust locator as per actual locator if different from above
        bolt_tshirt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        bolt_tshirt.click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )
        assert cart_count.text == '1'
        
        exit(0)  # Exit with code 0 if test case passed

    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)  # Exit with code 1 if test case failed

    finally:
        driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = '//*[@id="user-name"]'
        self.password_input = '//*[@id="password"]'
        self.login_button = '//*[@id="login-button"]'

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.username_input))
        ).send_keys(username)
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.password_input))
        ).send_keys(password)
        time.sleep(3)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.login_button))
        ).click()
        time.sleep(3)

if __name__ == "__main__":
    test_shopping_cart()
