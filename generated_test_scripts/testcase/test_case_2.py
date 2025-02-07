
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def wait_for_element(driver, by, locator):
    while True:
        try:
            element = driver.find_element(by, locator)
            return element
        except:
            time.sleep(1)

# Chrome options for headless mode, incognito, and disable notifications
options = Options()
options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Login Process
    wait_for_element(driver, By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    wait_for_element(driver, By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    wait_for_element(driver, By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Adding 'Bike Light' to cart
    wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)

    # Adding 'Fleece Jacket' to cart
    wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Verify cart badge count
    cart_count = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_count == '2', f"Expected cart count to be '2' but got '{cart_count}'"

    print("Test case passed")
    exit(0)

except Exception as e:
    print(f"Test case failed: {str(e)}")
    exit(1)

finally:
    driver.quit()
