
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = '//*[@id="user-name"]'
        self.password_locator = '//*[@id="password"]'
        self.login_button_locator = '//*[@id="login-button"]'

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_locator).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button_locator).click()

def test_purchase_flow():
    driver = webdriver.Chrome()
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        login_page = LoginPage(driver)

        # Login
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Add Bike Light
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)

        # Add Fleece Jacket
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)

        # Click on Cart Icon
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
        time.sleep(3)

        # Proceed to Checkout
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)

        # Enter User Information
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)

        # Click Continue
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
        time.sleep(3)

        # Complete the Purchase
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()
        time.sleep(3)

        # Return to Homepage
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))).click()
        time.sleep(3)

        # Logout
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
        time.sleep(3)
        return 0
    except Exception as e:
        print(f"Test failed: {e}")
        return 1
    finally:
        driver.quit()

if __name__ == "__main__":
    result = test_purchase_flow()
    if result == 0:
        print("Test case passed.")
    else:
        print("Test case failed.")
