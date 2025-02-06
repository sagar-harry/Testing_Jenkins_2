
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_payment_information_visibility():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    try:
        # Log in to the UI
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Wait for 3 seconds before every action
        time.sleep(3)
        
        # Add 'Bike Light' to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        
        # Add 'Fleece Jacket' to the cart
        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()
        
        # Proceed to checkout
        cart_icon = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        )
        cart_icon.click()

        time.sleep(3)
        
        checkout_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        )
        checkout_button.click()
        
        # Enter checkout details
        first_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        last_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))
        )
        zip_code = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))
        )
        
        first_name.send_keys("somename")
        last_name.send_keys("lastname")
        zip_code.send_keys("123456")

        time.sleep(3)
        
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))
        )
        continue_button.click()
        
        # Verify 'Payment Information' label is visible
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        assert payment_info_label.is_displayed(), "Payment Information label is not visible."
        print("Test passed")
        sys.exit(0)

    except Exception as e:
        print("Test failed: ", str(e))
        sys.exit(1)

    finally:
        driver.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        )
        
        username_field.send_keys(username)
        password_field.send_keys(password)

        time.sleep(3)
        
        login_button.click()

if __name__ == "__main__":
    test_payment_information_visibility()
