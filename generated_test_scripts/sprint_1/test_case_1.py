
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def setup_browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    return driver

def login(driver):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

def add_to_cart(driver, product_xpath):
    driver.find_element(By.XPATH, product_xpath).click()
    time.sleep(3)

def verify_cart_count(driver, expected_count):
    element = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    actual_count = element.text
    assert actual_count == expected_count, f"Expected cart count {expected_count}, but got {actual_count}"
    time.sleep(3)

def empty_cart(driver):
    driver.find_element(By.XPATH, '//button[contains(text(),"Remove")]').click()
    time.sleep(3)

def main():
    driver = setup_browser()
    try:
        login(driver)

        add_to_cart(driver, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        add_to_cart(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        verify_cart_count(driver, '2')

        empty_cart(driver)
        time.sleep(3)
        verify_cart_count(driver, '')

        add_to_cart(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        verify_cart_count(driver, '1')

        driver.quit()
        exit(0)
    except AssertionError as e:
        print(e)
        driver.quit()
        exit(1)

if __name__ == "__main__":
    main()
