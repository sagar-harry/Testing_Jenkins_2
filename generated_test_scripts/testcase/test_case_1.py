
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

def test_purchase_flow():
    driver = webdriver.Chrome()
    try:
        # Step 1: Open login page
        driver.get("https://www.example.com/login")

        # Step 2: Log in
        login_page = LoginPage(driver)
        login_page.login("valid_user", "valid_password")

        # Step 3: Add items to cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()

        # Step 4: Go to cart
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

        # Step 5: Proceed to checkout
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

        # Step 6: Enter checkout information
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")

        # Step 7: Continue and complete purchase
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()

        # Step 8: Return to homepage
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))

        # Step 9: Log out
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
        
        print(0)
    except Exception as e:
        print(f"Test failed: {e}")
        print(-1)
    finally:
        driver.quit()

test_purchase_flow()
