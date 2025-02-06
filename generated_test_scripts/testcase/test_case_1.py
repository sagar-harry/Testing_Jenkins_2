
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    options = Options()
    options.headless = True
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    return driver

def wait_for_element(driver, by, value):
    time.sleep(3)  # Wait for 3 seconds before looking for the element
    return driver.find_element(by, value)

def test_purchase_flow():
    try:
        driver = setup_driver()

        # Open the website and wait
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Initial wait for the page to load
        driver.maximize_window()

        # Login
        username_field = wait_for_element(driver, By.XPATH, '//*[@id="user-name"]')
        password_field = wait_for_element(driver, By.XPATH, '//*[@id="password"]')
        login_button = wait_for_element(driver, By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys('standard_user')
        password_field.send_keys('secret_sauce')
        login_button.click()

        # Add items to cart
        bike_light = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = wait_for_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bike_light.click()
        fleece_jacket.click()

        # Proceed to cart
        cart_icon = wait_for_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()

        # Checkout process
        checkout_button = wait_for_element(driver, By.XPATH, '//*[@id="checkout"]')
        checkout_button.click()

        first_name_field = wait_for_element(driver, By.XPATH, '//*[@id="first-name"]')
        last_name_field = wait_for_element(driver, By.XPATH, '//*[@id="last-name"]')
        postal_code_field = wait_for_element(driver, By.XPATH, '//*[@id="postal-code"]')

        first_name_field.send_keys('somename')
        last_name_field.send_keys('lastname')
        postal_code_field.send_keys('123456')

        continue_button = wait_for_element(driver, By.XPATH, '//*[@id="continue"]')
        continue_button.click()

        # Finish purchase
        finish_button = wait_for_element(driver, By.XPATH, '//*[@id="finish"]')
        finish_button.click()

        # Return to homepage
        back_to_products = wait_for_element(driver, By.XPATH, '//*[@id="back-to-products"]')
        back_to_products.click()

        # Logout
        logout_sidebar = wait_for_element(driver, By.XPATH, '//*[@id="react-burger-menu-btn"]')
        logout_sidebar.click()
        time.sleep(3)
        logout_button = wait_for_element(driver, By.XPATH, '//*[@id="logout_sidebar_link"]')
        logout_button.click()

        driver.quit()
        exit(0)  # Test case passed

    except Exception as e:
        print(e)
        driver.quit()
        exit(1)  # Test case failed

if __name__ == "__main__":
    test_purchase_flow()
