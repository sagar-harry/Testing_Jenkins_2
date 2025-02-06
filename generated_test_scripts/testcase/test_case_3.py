
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver):
    driver.get("https://saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def run_test():
    try:
        options = Options()
        options.headless = True
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)
        
        driver.maximize_window()
        login(driver)
        
        # Wait for the page to load
        time.sleep(5)

        # Add 'Bike Light' to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Verify cart badge displays '2'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '2', "Cart count is incorrect"
        
        # Reset the cart
        driver.find_element(By.ID, 'shopping_cart_container').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'continue-shopping')))
        driver.find_element(By.ID, 'continue-shopping').click()
        time.sleep(3)
        
        # Verify cart is empty
        cart_badge = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_badge) == 0, "Cart is not empty after reset"

        # Add 'Bolt T-Shirt' to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Verify cart badge displays '1'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '1', "Cart count is incorrect after adding Bolt T-Shirt"

        driver.quit()
        exit(0)
    except Exception as e:
        print("Test failed:", str(e))
        driver.quit()
        exit(1)

if __name__ == "__main__":
    run_test()
