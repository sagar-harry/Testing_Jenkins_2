
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = "//*[@id='user-name']"
        self.password_input = "//*[@id='password']"
        self.login_button = "//*[@id='login-button']"

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(3)


def test_complete_purchase_flow():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")  # Example URL, replace with the actual login URL

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")  # Replace with valid credentials

    # Add Bike Light to the cart
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(3)

    # Add Fleece Jacket to the cart
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    time.sleep(3)

    # Click on the cart icon
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
    time.sleep(3)

    # Proceed to checkout
    driver.find_element(By.XPATH, "//*[@id='checkout']").click()
    time.sleep(3)

    # Enter user details
    driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("somename")
    driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("lastname")
    driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("123456")
    driver.find_element(By.XPATH, "//*[@id='continue']").click()
    time.sleep(3)

    # Complete the purchase
    driver.find_element(By.XPATH, "//*[@id='finish']").click()
    time.sleep(3)

    # Return to the homepage
    driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()
    time.sleep(3)

    # Click on logout sidebar
    driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
    time.sleep(3)

    # Click on logout button
    driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()
    time.sleep(3)

    # Verify successful logout
    assert "https://www.saucedemo.com/" in driver.current_url

    driver.quit()

if __name__ == "__main__":
    test_complete_purchase_flow()
