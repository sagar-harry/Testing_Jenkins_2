
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        login_button.click()

def test_add_items_to_cart():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Assuming ChromeDriver is in the PATH
    driver.get("https://www.example.com/login")  # Replace with the actual URL
    driver.maximize_window()

    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Wait for login to complete and element to be clickable
    try:
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        
        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        bike_light_button.click()
        time.sleep(1)  # Adding slight delay to ensure synchronization
        fleece_jacket_button.click()

        # Verify the cart count
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )

        if cart_count.text == '2':
            print("Test Passed: Cart displays 2 items")
            driver.quit()
            return 0
        else:
            print("Test Failed: Cart count is incorrect")
            driver.quit()
            return -1

    except Exception as e:
        print(f"Test Failed: {e}")
        driver.quit()
        return -1

if __name__ == "__main__":
    result = test_add_items_to_cart()
    exit(result)
