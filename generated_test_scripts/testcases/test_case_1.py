
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        
        # Maximize the window
        driver.maximize_window()
        
        # Login
        time.sleep(3)
        LoginPage.login(driver, "standard_user", "secret_sauce")

        # Add Bike Light and Fleece Jacket to the cart
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()

        # Open Cart
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

        # Checkout
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='checkout']").click()

        # Enter User Info
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("somename")
        driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("lastname")
        driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("123456")

        # Continue and Finish Purchase
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='continue']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='finish']").click()

        # Return to Homepage
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()

        # Logout
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()
        
        # Test Passed
        exit(0)

    except NoSuchElementException:
        # Test Failed
        exit(1)
    finally:
        driver.quit()

class LoginPage:
    @staticmethod
    def login(driver, username, password):
        driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='login-button']").click()

if __name__ == "__main__":
    run_test()
