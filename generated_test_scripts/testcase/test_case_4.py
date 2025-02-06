
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

URL = "https://saucedemo.com/"

# Setting up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-infobars")

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)

# Function to log in
class LoginPage:
    @staticmethod
    def login(username, password):
        driver.get(URL)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(3)

        # Locate username and password fields and login button
        user_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        pass_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_btn = driver.find_element(By.XPATH, '//*[@id="login-button"]')

        user_input.send_keys(username)
        time.sleep(3)
        pass_input.send_keys(password)
        time.sleep(3)
        login_btn.click()
        time.sleep(3)

def test_checkout_flow():
    try:
        # Log in
        LoginPage.login("standard_user", "secret_sauce")

        # Add items to the cart
        bike_light = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)

        # Proceed to checkout
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)

        checkout_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]')))
        checkout_btn.click()
        time.sleep(3)

        # Enter checkout information
        first_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

        first_name_field.send_keys("somename")
        time.sleep(3)
        last_name_field.send_keys("lastname")
        time.sleep(3)
        zip_code_field.send_keys("123456")
        time.sleep(3)

        # Continue to next step
        continue_btn = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_btn.click()
        time.sleep(3)

        # Verify payment information is visible
        payment_info_label = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
        
        if payment_info_label.is_displayed():
            print("Payment Information label is visible.")
            driver.quit()
            exit(0)
        else:
            print("Payment Information label is not visible.")
            driver.quit()
            exit(1)

    except Exception as e:
        print("Test failed due to an exception.")
        traceback.print_exc()
        driver.quit()
        exit(1)

if __name__ == "__main__":
    test_checkout_flow()
