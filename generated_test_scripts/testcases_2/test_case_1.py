
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        login(driver)

        # Add Bike Light and Fleece Jacket to cart
        wait_and_click(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        wait_and_click(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        # Click on cart icon
        wait_and_click(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a')

        # Proceed to checkout
        wait_and_click(driver, By.XPATH, '//*[@id="checkout"]')
        wait_and_fill(driver, By.XPATH, '//*[@id="first-name"]', 'somename')
        wait_and_fill(driver, By.XPATH, '//*[@id="last-name"]', 'lastname')
        wait_and_fill(driver, By.XPATH, '//*[@id="postal-code"]', '123456')

        # Continue and complete purchase
        wait_and_click(driver, By.XPATH, '//*[@id="continue"]')
        wait_and_click(driver, By.XPATH, '//*[@id="finish"]')

        # Return to homepage
        wait_and_click(driver, By.XPATH, '//*[@id="back-to-products"]')

        # Logout
        wait_and_click(driver, By.XPATH, '//*[@id="react-burger-menu-btn"]')
        wait_and_click(driver, By.XPATH, '//*[@id="logout_sidebar_link"]')

        exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)
    finally:
        driver.quit()

def login(driver):
    wait_and_fill(driver, By.XPATH, '//*[@id="user-name"]', 'standard_user')
    wait_and_fill(driver, By.XPATH, '//*[@id="password"]', 'secret_sauce')
    wait_and_click(driver, By.XPATH, '//*[@id="login-button"]')

def wait_and_click(driver, by, value):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
    time.sleep(3)
    driver.find_element(by, value).click()

def wait_and_fill(driver, by, value, text):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))
    time.sleep(3)
    driver.find_element(by, value).send_keys(text)

if __name__ == "__main__":
    main()
