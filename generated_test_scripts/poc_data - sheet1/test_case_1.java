
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.concurrent.TimeUnit;

public class LoginTest {

    public static void main(String[] args) {
        // Set up Chrome options
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--incognito");
        options.addArguments("--disable-notifications");
        options.addArguments("--disable-popup-blocking");

        // Initialize WebDriver
        WebDriver driver = new ChromeDriver(options);

        try {
            // Maximize
            driver.manage().window().maximize();

            // Open page
            driver.get("https://practicetestautomation.com/practice-test-login/");
            TimeUnit.SECONDS.sleep(5);

            WebDriverWait wait = new WebDriverWait(driver, 10);

            // Username input
            WebElement usernameField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@name='username']")));
            TimeUnit.SECONDS.sleep(3);
            usernameField.sendKeys("student");

            // Password input
            WebElement passwordField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@name='password']")));
            TimeUnit.SECONDS.sleep(3);
            passwordField.sendKeys("Password123");

            // Submit button
            WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//button[@type='submit']")));
            TimeUnit.SECONDS.sleep(3);
            submitButton.click();

            // Verification of successful login
            WebElement logoutButton = wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("Log out")));
            TimeUnit.SECONDS.sleep(3);
            if (logoutButton.isDisplayed()) {
                System.out.println("Test Passed");
                System.exit(0);
            } else {
                System.out.println("Test Failed");
                System.exit(1);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Test Failed");
            System.exit(1);
        } finally {
            driver.quit();
        }
    }
}
