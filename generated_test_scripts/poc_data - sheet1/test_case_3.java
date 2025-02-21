
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import java.util.concurrent.TimeUnit;

public class InvalidPasswordTest {
    public static void main(String[] args) {
        // Setting up Chrome Options
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--disable-notifications");
        options.addArguments("--incognito");
        
        // Initialize WebDriver
        WebDriver driver = new ChromeDriver(options);
        try {
            // Open the page
            driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
            driver.get("http://yourwebsite.com/login");  // replace with the actual URL
            driver.manage().window().maximize();
            Thread.sleep(5000); // Wait for 5 seconds after opening the page

            // Enter username
            WebElement usernameField = driver.findElement(By.xpath("//input[@name='username']"));
            usernameField.sendKeys("student");
            Thread.sleep(3000); // Wait for 3 seconds

            // Enter invalid password
            WebElement passwordField = driver.findElement(By.xpath("//input[@name='password']"));
            passwordField.sendKeys("incorrectPassword");
            Thread.sleep(3000); // Wait for 3 seconds

            // Click submit
            WebElement submitButton = driver.findElement(By.xpath("//button[@type='submit']"));
            submitButton.click();
            Thread.sleep(3000); // Wait for 3 seconds

            // Verify error message for invalid password
            WebElement errorMessage = driver.findElement(By.id("error")); // Replace with actual error message locator
            if (errorMessage.isDisplayed()) {
                System.out.println("Test Case Passed");
                System.exit(0);
            } else {
                System.out.println("Test Case Failed");
                System.exit(1);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        } finally {
            // Close the browser
            driver.quit();
        }
    }
}
