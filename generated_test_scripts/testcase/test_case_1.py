
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()

def main():
    try:
        # Chrome options
        options = Options()
        options.headless = True
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        # Driver setup
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")

        # Initial wait and setup
        time.sleep(5)
        driver.maximize_window()

        # Page Object for Login
        login_page = LoginPage(driver)

        # Login
        time.sleep(3)
        login_page.login('standard_user', 'secret_sauce')

        # Adding items to cart
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()

        # Proceed to cart
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

        # Checkout
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='checkout']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys('somename')
        driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys('lastname')
        driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys('123456')
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='continue']").click()

        # Finish purchase
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='finish']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()

        # Logout
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()

        driver.quit()
        sys.exit(0)

    except Exception as e:
        print(e)
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
