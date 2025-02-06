
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def test_ui_scenario():
    driver = webdriver.Chrome()
    driver.get("https://www.yourwebsite.com")
    time.sleep(5)  # Wait for the page to load
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        
        # Login
        login_page.login("testuser", "testpassword")
        time.sleep(3)

        # Add products to cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)

        # Go to cart
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        ).click()
        time.sleep(3)

        # Proceed to checkout
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        ).click()
        time.sleep(3)

        # Enter checkout information
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        ).send_keys("somename")
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        time.sleep(3)
        
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
        time.sleep(3)

        # Continue to payment information
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Verify that the payment information label is visible
        payment_info_visible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )
        if payment_info_visible:
            print("Test Case Passed")
            return 0
        else:
            print("Test Case Failed")
            return 1

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    result = test_ui_scenario()
    exit(result)
