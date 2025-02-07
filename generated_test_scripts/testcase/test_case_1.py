
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_ui_purchase_flow():
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-notifications')
        options.add_argument('--incognito')
        
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)

        driver.get('https://saucedemo.com/')
        time.sleep(5)

        driver.maximize_window()

        # Login
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

        # Add items to cart
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        
        # Proceed to cart and checkout
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

        # Enter checkout information
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()

        # Complete purchase
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        
        # Go back to products page
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()

        # Logout
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

        time.sleep(3)
        driver.quit()
        exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        if driver:
            driver.quit()
        exit(1)

if __name__ == "__main__":
    test_ui_purchase_flow()
