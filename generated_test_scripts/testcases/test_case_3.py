
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    try:
        # Set up options for headless mode, disable notifications, pop ups and run incognito
        options = Options()
        options.headless = True
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--incognito")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=options)

        # Open a specific URL (replace 'your_url_here' with the actual URL)
        driver.get('your_url_here')

        # Wait for 5 seconds after opening the page
        time.sleep(5)

        # Maximize the browser window
        driver.maximize_window()

        # Wait for 3 secs before action
        time.sleep(3)

        # Example of waiting for an element - replace 'your_element_locator' and 'By.ID' as needed
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'your_element_locator'))
        )

        # Perform actions here (click, input, etc.)
        # For example: element.click()
        
        # Again wait for 3 secs before any other action
        time.sleep(3)

        # Exit with success code
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        # Ensure the browser is closed
        driver.quit()

if __name__ == "__main__":
    run_test()
