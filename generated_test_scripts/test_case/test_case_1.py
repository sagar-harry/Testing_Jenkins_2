
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Initialize WebDriver
driver = webdriver.Chrome()

# Define a function to login using credentials
def login(username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

# Open the login page
driver.get("http://example.com/login")  # Replace with actual URL

# Test Case: Validate complete purchase flow and logout
def test_purchase_and_logout():
    try:
        # Step 1: Login
        login("valid_username", "valid_password")

        # Step 2: Add items to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Step 3: Go to the cart and checkout
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").click()
        driver.find_element(By.ID, "checkout").click()

        # Step 4: Enter checkout information
        driver.find_element(By.ID, "first-name").send_keys("somename")
        driver.find_element(By.ID, "last-name").send_keys("lastname")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Step 5: Complete the purchase
        driver.find_element(By.ID, "finish").click()
        sleep(2)  # Wait for the purchase to complete

        # Step 6: Return to home page
        driver.find_element(By.ID, "back-to-products").click()

        # Step 7: Logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        sleep(1)  # Wait for menu animation
        driver.find_element(By.ID, "logout_sidebar_link").click()

    finally:
        driver.quit()

# Run the test case
test_purchase_and_logout()
