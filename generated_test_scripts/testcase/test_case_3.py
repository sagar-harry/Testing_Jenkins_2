
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        time.sleep(3)  # wait for the page to load

def test_ui_scenario():
    # Initialize the webdriver
    driver = webdriver.Chrome()

    try:
        # Open the page
        driver.get('https://www.example.com/')
        driver.maximize_window()
        time.sleep(5)  # Wait for 5 seconds

        # Create a LoginPage object and login
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')
        
        # Add 'Bike Light' to the cart
        bike_light = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
        bike_light.click()
        time.sleep(3)  # Wait for action to complete
        
        # Add 'Fleece Jacket' to the cart
        fleece_jacket = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
        fleece_jacket.click()
        time.sleep(3)  # Wait for action to complete

        # Verify cart badge count is '2'
        cart_count = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
        if cart_count.text != '2':
            return -1

        # Reset the cart (remove the added products)
        # Assuming there's a method to reset the cart, typically via a URL or button
        reset_button = driver.find_element(By.XPATH, "//*[@id='reset-cart-button']")
        reset_button.click()
        time.sleep(3)  # Wait for action to complete

        # Verify the cart is empty
        if cart_count.is_displayed():
            return -1

        # Add 'Bolt T-Shirt' to the cart after reset
        bolt_t_shirt = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        bolt_t_shirt.click()
        time.sleep(3)  # Wait for action to complete

        # Verify cart badge count is '1'
        if cart_count.text != '1':
            return -1

        return 0

    except Exception as e:
        print("An error occurred:", str(e))
        return -1

    finally:
        driver.quit()

# Run the test
result = test_ui_scenario()
print("Test Result:", "Passed" if result == 0 else "Failed")
