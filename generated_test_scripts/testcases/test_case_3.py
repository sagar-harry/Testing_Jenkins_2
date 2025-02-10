
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_cart_functionality():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        # Set up the WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Open the website
            driver.get("https://saucedemo.com/")
            time.sleep(5)  # Wait for 5 secs

            # Maximize the window
            driver.maximize_window()

            # Log in to the application
            login(driver)

            # Add 'Bike Light' to the cart
            wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
            time.sleep(3)

            # Add 'Fleece Jacket' to the cart
            wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
            time.sleep(3)

            # Verify cart badge displays '2'
            cart_count = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
            assert cart_count == '2', "Cart badge did not display '2'"

            # Reset the cart
            remove_items_from_cart(driver)

            # Verify the cart is empty
            cart_count = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert len(cart_count) == 0, "Cart is not empty"

            # Add 'Bolt T-Shirt' to the cart after reset
            wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
            time.sleep(3)

            # Verify cart badge displays '1'
            cart_count = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
            assert cart_count == '1', "Cart badge did not display '1'"

            # Exit with code 0 if test case passed
            return 0
            
        finally:
            # Quit the driver
            driver.quit()

    except Exception as e:
        print(f"Test failed: {e}")
        # Exit with code 1 if test case failed
        return 1

def login(driver):
    wait_for_element(driver, By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    wait_for_element(driver, By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    wait_for_element(driver, By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

def remove_items_from_cart(driver):
    # Navigate to cart and remove items
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
    time.sleep(3)
    remove_buttons = driver.find_elements(By.XPATH, '//button[text()="Remove"]')
    for button in remove_buttons:
        button.click()
        time.sleep(3)

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

# Run the test case
exit(test_cart_functionality())
