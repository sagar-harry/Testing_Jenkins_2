
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def wait_for_element(driver, locator):
    attempts = 0
    while attempts < 5:
        try:
            element = driver.find_element(By.XPATH, locator)
            return element
        except:
            time.sleep(1)
            attempts += 1
    return None

def test_complete_purchase_flow():
    driver = setup_driver()

    try:
        # Step 1: Open the website and login
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        wait_for_element(driver, '//*[@id="user-name"]').send_keys("standard_user")
        wait_for_element(driver, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        wait_for_element(driver, '//*[@id="login-button"]').click()

        # Step 2: Add items to the cart
        time.sleep(3)
        wait_for_element(driver, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        wait_for_element(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

        # Step 3: Click on the cart icon
        time.sleep(3)
        wait_for_element(driver, '//*[@id="shopping_cart_container"]/a').click()

        # Step 4: Proceed to checkout
        time.sleep(3)
        wait_for_element(driver, '//*[@id="checkout"]').click()

        # Step 5: Enter user information
        time.sleep(3)
        wait_for_element(driver, '//*[@id="first-name"]').send_keys("somename")
        wait_for_element(driver, '//*[@id="last-name"]').send_keys("lastname")
        wait_for_element(driver, '//*[@id="postal-code"]').send_keys("123456")

        # Step 6: Continue and finish purchase
        time.sleep(3)
        wait_for_element(driver, '//*[@id="continue"]').click()
        time.sleep(3)
        wait_for_element(driver, '//*[@id="finish"]').click()

        # Step 7: Return to homepage and logout
        time.sleep(3)
        wait_for_element(driver, '//*[@id="back-to-products"]').click()
        time.sleep(3)
        wait_for_element(driver, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        wait_for_element(driver, '//*[@id="logout_sidebar_link"]').click()

        # Test passed
        driver.quit()
        exit(0)

    except Exception as e:
        print(f"Test failed: {str(e)}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    test_complete_purchase_flow()
