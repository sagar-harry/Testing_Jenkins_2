
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def run_ui_test():
    # Configure Selenium WebDriver options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    
    try:
        # Open the website
        driver.get("https://saucedemo.com/")
        # Maximize window
        driver.maximize_window()
        # Wait for the page to load (5 seconds)
        sleep(5)

        # Wait and perform login
        login(driver)

        # Wait before action
        sleep(3)

        # Add 'Bike Light' to cart
        add_item_to_cart(driver, '//*[@id="add-to-cart-sauce-labs-bike-light"]')

        # Wait before action
        sleep(3)

        # Add 'Fleece Jacket' to cart
        add_item_to_cart(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        # Wait before action
        sleep(3)

        # Verify cart badge displays '2'
        verify_cart_count(driver, '//*[@id="shopping_cart_container"]/a/span', '2')

        # Exit with success
        exit(0)
        
    except Exception as e:
        print(f"Test failed: {e}")
        # Exit with error
        exit(1)
    finally:
        driver.quit()

def login(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    ).send_keys('your_username')
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
    ).send_keys('your_password')
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
    ).click()

def add_item_to_cart(driver, item_xpath):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, item_xpath))
    ).click()

def verify_cart_count(driver, cart_counter_xpath, expected_count):
    cart_count_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, cart_counter_xpath))
    )
    actual_count = cart_count_element.text
    assert actual_count == expected_count, f"Cart count mismatch: expected {expected_count}, got {actual_count}"

if __name__ == "__main__":
    run_ui_test()
