
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)

    username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]')))

    username_input.send_keys("standard_user")
    time.sleep(3)
    password_input.send_keys("secret_sauce")
    time.sleep(3)
    login_button.click()

def test_checkout_flow():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)

    try:
        login(driver)

        wait = WebDriverWait(driver, 30)

        bike_light = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        time.sleep(3)

        fleece_jacket = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket.click()
        time.sleep(3)

        cart_icon = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        cart_icon.click()
        time.sleep(3)

        checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]')))
        checkout_button.click()
        time.sleep(3)

        first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]')))
        zip_code = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]')))

        first_name.send_keys("somename")
        time.sleep(3)
        last_name.send_keys("lastname")
        time.sleep(3)
        zip_code.send_keys("123456")
        time.sleep(3)

        continue_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]')))
        continue_button.click()
        time.sleep(3)

        payment_info_label = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))

        assert payment_info_label.is_displayed()
        exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)

    finally:
        driver.quit()

test_checkout_flow()
