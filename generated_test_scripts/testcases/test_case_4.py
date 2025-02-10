
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def test_check_payment_information():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--incognito')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.maximize_window()
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        
        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')
        
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        time.sleep(3)
        
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)
        
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)
        
        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout_button.click()
        time.sleep(3)
        
        first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        
        first_name_field.send_keys('somename')
        time.sleep(3)
        last_name_field.send_keys('lastname')
        time.sleep(3)
        zip_code_field.send_keys('123456')
        time.sleep(3)
        
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)
        
        payment_info_label = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
        
        if payment_info_label.is_displayed():
            exit(0)
        else:
            exit(1)
            
    except Exception as e:
        print("Test case failed:", str(e))
        exit(1)
        
    finally:
        driver.quit()

test_check_payment_information()
