
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
        self.wait_for_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.wait_for_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.wait_for_element(By.XPATH, '//*[@id="login-button"]').click()

    def wait_for_element(self, by, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))

def run_test():
    # Set up chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')

    # Initialize webdriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    driver.implicitly_wait(10)
    time.sleep(5)

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Assert cart badge displays '2'
        cart_count = login_page.wait_for_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '2', "Cart count should be '2'. Found: " + cart_count

        # Reset the cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/div[3]/button').click()
        time.sleep(3)

        # Check if the cart is empty
        cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
        assert len(cart_items) == 0, "Cart should be empty after reset."

        # Add 'Bolt T-Shirt' to the cart after reset
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Assert cart badge displays '1'
        cart_count = login_page.wait_for_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '1', "Cart count should be '1'. Found: " + cart_count

        print("Test case passed")
        exit(0)

    except AssertionError as ae:
        print(f"Assertion Error: {ae}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
