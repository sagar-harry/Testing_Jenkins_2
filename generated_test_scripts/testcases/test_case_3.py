
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def test_ui_scenario():
    try:
        # Set up Chrome options for headless mode, incognito, and pop-up blocking
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the website
        driver.get('https://saucedemo.com/')
        time.sleep(5)  # Wait for 5 seconds
        
        # Login
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

        # Add 'Bike Light' to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '2', f"Expected cart count to be 2, but got {cart_count}"
        
        # Reset cart
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
        time.sleep(3)

        # Verify cart is empty (cart badge should not be displayed)
        cart_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_elements) == 0, "Expected cart to be empty, but items are still present."

        # Add 'Bolt T-Shirt' to cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge displays '1'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '1', f"Expected cart count to be 1, but got {cart_count}"

        # Test passed
        driver.quit()
        sys.exit(0)

    except AssertionError as e:
        print(f"Assertion Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_ui_scenario()
