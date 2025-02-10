
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        password_field.send_keys(password)
        sleep(3)
        login_button.click()
        sleep(3)

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    
    driver = webdriver.Chrome(options=options)
    driver.get('https://saucedemo.com/')
    driver.maximize_window()
    sleep(5)

    # Login to application
    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    try:
        # Add Bike Light and Fleece Jacket to the cart
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        sleep(3)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        sleep(3)

        # Verify the cart badge is 2
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        ).text
        assert cart_count == '2'
        sleep(3)

        # Reset the cart (remove the added products)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        sleep(3)

        driver.find_element(By.ID, "reset_sidebar_link").click()
        sleep(3)

        # Verify the cart is empty
        cart_badge = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert not cart_badge
        sleep(3)

        # Add Bolt T-Shirt to the cart after reset
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]'))
        ).click()
        sleep(3)

        # Verify the cart badge is 1
        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        ).text
        assert cart_count == '1'
        sleep(3)

        driver.quit()
        exit(0)

    except AssertionError as e:
        driver.quit()
        exit(1)

if __name__ == "__main__":
    main()
