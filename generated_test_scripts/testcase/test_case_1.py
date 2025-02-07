
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

try:
    # Chrome options for headless mode, disable notifications, pop-ups, and incognito
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the website and maximize window
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Wait for 3 secs before every action
    time.sleep(3)

    # Log in to the application
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add items to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)  
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)  
    
    # Go to the cart
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    
    # Proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)
    
    # Enter user information
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
    time.sleep(3)
    
    # Continue and complete purchase
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)
    
    # Return to homepage and logout
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    # Successful test completion
    driver.quit()
    exit(0)

except Exception as e:
    print(e)
    driver.quit()
    exit(1)
