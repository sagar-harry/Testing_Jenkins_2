
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        sleep(3)

def test_scenario():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    sleep(5)
    driver.maximize_window()
    
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    # Add "Bike Light" and "Fleece Jacket" to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    sleep(3)

    # Verify the cart badge displays "2"
    cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_count == '2', "Test Failed: Cart does not show '2'"
    
    # Reset cart (remove added products)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()
    sleep(3)

    # Verify the cart is empty
    driver.back()
    sleep(3)
    cart_count_empty = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert len(cart_count_empty) == 0, "Test Failed: Cart is not empty after reset"
    
    # Add 'Bolt T-Shirt' to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    sleep(3)

    # Verify the cart badge displays "1"
    cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_count == '1', "Test Failed: Cart does not show '1'"
    
    print("Test Passed")
    driver.quit()
    sys.exit(0)

try:
    test_scenario()
except AssertionError as e:
    print(str(e))
    sys.exit(1)
except Exception as e:
    print("An error occurred:", str(e))
    sys.exit(1)
