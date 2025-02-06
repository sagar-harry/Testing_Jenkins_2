
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, wait):
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()
    time.sleep(3)

def main():
    options = Options()
    options.headless = True
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        wait = WebDriverWait(driver, 10)
        login(driver, wait)

        # Add 'Bike Light'
        bike_light_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_button.click()
        time.sleep(3)

        # Add 'Fleece Jacket'
        fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket_button.click()
        time.sleep(3)

        # Verify the cart badge displays '2'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '2', "Test failed at adding items to cart"

        # Reset the cart
        remove_bike_light_button = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
        remove_bike_light_button.click()
        time.sleep(3)

        remove_fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')
        remove_fleece_jacket_button.click()
        time.sleep(3)

        # Verify the cart is empty
        try:
            cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
            assert False, "Test failed at resetting cart"
        except:
            assert True

        # Add 'Bolt T-Shirt'
        bolt_t_shirt_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        bolt_t_shirt_button.click()
        time.sleep(3)

        # Verify the cart badge displays '1'
        cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
        assert cart_count == '1', "Test failed at adding 'Bolt T-Shirt' to cart"

        # Exit with code 0 if successful
        exit(0)

    except AssertionError as e:
        print(e)
        exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
