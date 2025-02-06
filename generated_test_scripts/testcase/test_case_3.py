
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()

def test_cart_functionality():
    try:
        # Initialize WebDriver
        driver = webdriver.Chrome()
        driver.get("https://www.example.com")  # Replace with the actual URL

        # Log in
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Wait for login - Assuming login leads to homepage
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='menu_button_container']")))

        # Add Bike Light to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))).click()

        # Add Fleece Jacket to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()

        # Verify cart badge is '2'
        badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))

        if badge.text != '2':
            raise AssertionError("Cart badge should display '2'. Current value: {}".format(badge.text))

        # Reset the cart - Assuming a reset is done by removing items
        # Remove all items one by one
        driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-bike-light']").click()
        driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-bolt-t-shirt']").click()

        time.sleep(2)  # Wait for UI to update

        # Verify the cart is empty
        try:
            badge = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
            if badge.text != '':
                raise AssertionError("Cart should be empty. Current cart badge: {}".format(badge.text))
        except Exception:
            pass  # No badge means cart is empty

        # Add Bolt T-Shirt to cart after reset
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()

        # Verify cart badge is '1'
        badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))

        if badge.text != '1':
            raise AssertionError("Cart badge should display '1'. Current value: {}".format(badge.text))

        print("Test passed")
        return 0

    except Exception as e:
        print(f"Test failed: {str(e)}")
        return -1

    finally:
        # Cleanup
        driver.quit()

if __name__ == "__main__":
    result = test_cart_functionality()
    exit(result)
