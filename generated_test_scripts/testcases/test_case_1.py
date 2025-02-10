
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--incognito')

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Function to wait for an element
    def wait_for_element(by, locator):
        timeout = 10
        while timeout > 0:
            elements = driver.find_elements(by, locator)
            if len(elements) > 0:
                return elements[0]
            else:
                time.sleep(1)
                timeout -= 1
        raise Exception(f"Element not found: {locator}")

    # Login
    wait_for_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    wait_for_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    wait_for_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add items to cart
    wait_for_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    wait_for_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Proceed to cart and checkout
    wait_for_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    wait_for_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    # Enter checkout information
    wait_for_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
    time.sleep(3)
    wait_for_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
    time.sleep(3)
    wait_for_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
    time.sleep(3)

    # Continue and finish
    wait_for_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)
    wait_for_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    # Return to homepage
    wait_for_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    # Logout
    wait_for_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    wait_for_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    # Exit with successful execution
    driver.quit()
    exit(0)

except Exception as e:
    print(str(e))
    driver.quit()
    exit(1)
