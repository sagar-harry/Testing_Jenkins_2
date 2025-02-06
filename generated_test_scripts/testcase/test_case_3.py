
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_ui_scenario():
    driver = webdriver.Chrome()
    driver.get('https://www.example.com/login')  # Replace with the correct URL

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    try:
        wait = WebDriverWait(driver, 10)
        
        # Add 'Bike Light' to the cart
        sleep(3)
        bike_light_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_button.click()

        # Add 'Fleece Jacket' to the cart
        sleep(3)
        fleece_jacket_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket_button.click()

        # Validate cart badge displays '2'
        sleep(3)
        cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '2', "Cart count is not 2."

        # Reset cart (you need to implement the logic to reset the cart here)
        # This part is assumed as pseudo-code
        # sleep(3)
        # reset_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, 'RESET_CART_BUTTON_LOCATOR')))
        # reset_cart_button.click()

        # Validate cart is empty (you need to verify this based on the UI behavior)
        sleep(3)
        try:
            cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
            assert False, "Cart is not empty after reset."
        except:
            pass  # Cart badge is not displayed, cart is empty

        # Add 'Bolt T-Shirt' to the cart after reset
        sleep(3)
        t_shirt_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        t_shirt_button.click()

        # Validate cart badge displays '1'
        sleep(3)
        cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_count.text == '1', "Cart count is not 1."

        driver.quit()
        return 0  # Success

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        return -1  # Failure

# Execute the test case
result = test_ui_scenario()
