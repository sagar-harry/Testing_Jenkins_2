
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = "username"
        self.password = "password"
    
    def login(self):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(self.username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    def logout(self):
        self.driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)  # Wait for the sidebar to open
        self.driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

class PurchaseFlowTest:
    def __init__(self, driver):
        self.driver = driver
    
    def test_purchase_flow(self):
        login_page = LoginPage(self.driver)
        
        # Login
        login_page.login()
        time.sleep(3)
        
        # Add items to the cart
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        
        # Proceed to checkout
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)
        
        # Enter checkout information
        self.driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
        self.driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
        self.driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)
        
        # Complete the purchase
        self.driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)
        
        # Return to homepage
        self.driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
        time.sleep(3)
        
        # Logout
        login_page.logout()
        time.sleep(3)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('http://example.com/login')  # Replace with the actual URL of the login page
    purchase_flow_test = PurchaseFlowTest(driver)
    purchase_flow_test.test_purchase_flow()
    driver.quit()
