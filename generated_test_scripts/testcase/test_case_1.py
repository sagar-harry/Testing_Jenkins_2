
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def test_purchase_flow():
    options = Options()
    options.headless = True
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Adding items to cart
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

        # Complete purchase
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        time.sleep(3)

        # Logout
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
        time.sleep(3)

        driver.quit()
        exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    test_purchase_flow()
