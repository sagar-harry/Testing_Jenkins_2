
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up headless, incognito browser
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)

try:
    # Open the URL
    driver.get('https://saucedemo.com/')
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Maximize the page
    driver.maximize_window()

    # Log in
    def login():
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

    login()
    
    # Add 'Bike Light'
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)  # Wait for action

    # Add 'Fleece Jacket'
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Verify cart badge displays '2'
    cart_count_element = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    if cart_count_element.text != '2':
        raise Exception("Cart badge should display '2'")

    # Reset cart (by removing products manually or using a reset button)
    for remove_button in driver.find_elements(By.XPATH, '//*[contains(@id, "remove-sauce-labs")]'):
        remove_button.click()
        time.sleep(3)

    # Verify the cart is empty
    empty_cart_badge = len(driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    if empty_cart_badge != 0:
        raise Exception("Cart should be empty")

    # Add 'Bolt T-Shirt' after reset
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Verify cart badge displays '1'
    cart_count_element = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    if cart_count_element.text != '1':
        raise Exception("Cart badge should display '1'")

    # Test passed    
    driver.quit()
    exit(0)

except Exception as e:
    print(str(e))
    driver.quit()
    exit(1)
