
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def test_checkout_flow():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open website
        driver.get('https://saucedemo.com/')
        time.sleep(5)

        # Maximize the page
        driver.maximize_window()

        # Login
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        # Add items to the cart
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Proceed to checkout
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        # Enter checkout information
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Verify 'Payment Information' label is visible
        payment_label = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        assert payment_label.is_displayed(), "Payment Information label is not visible"

        print("Test Case Passed")
        sys.exit(0)  # Test case passed

    except Exception as e:
        print(f"Test Case Failed: {str(e)}")
        sys.exit(1)  # Test case failed

    finally:
        # Quit the browser
        driver.quit()

if __name__ == "__main__":
    test_checkout_flow()
