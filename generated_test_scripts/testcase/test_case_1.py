
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        login(driver)

        # Add items to cart
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        time.sleep(3)

        # Go to cart and checkout
        driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='checkout']").click()
        time.sleep(3)

        # Enter customer information
        driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("123456")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='continue']").click()
        time.sleep(3)

        # Finish and return to homepage
        driver.find_element(By.XPATH, "//*[@id='finish']").click()
        time.sleep(3)
        
        # Log out
        driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()
        
        print("Test passed")
        exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)
        
    finally:
        driver.quit()

def login(driver):
    driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='login-button']").click()
    time.sleep(3)

if __name__ == "__main__":
    main()
