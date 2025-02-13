
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        ).send_keys(username)
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        ).send_keys(password)
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        ).click()
        time.sleep(3)

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-popup-blocking')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://saucedemo.com/")
    time.sleep(5)

    login_page = LoginPage(driver)
    try: 
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        ).send_keys('somename')
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))
        ).send_keys('lastname')
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))
        ).send_keys('123456')
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))
        ).click()
        
        print("Test Passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
