
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def setup_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-popup-blocking')
    driver = webdriver.Chrome(options=options)
    return driver

def login(driver, username, password):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

def perform_test():
    driver = setup_driver()
    try:
        login(driver, "standard_user", "secret_sauce")
        
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        payment_information = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        if payment_information.is_displayed():
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)
    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    perform_test()
