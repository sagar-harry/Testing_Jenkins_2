
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.WebElement;
import java.util.concurrent.TimeUnit;

public class LoginTest {

    public static void main(String[] args) {
        // Set up ChromeOptions for headless mode, incognito mode, and disabling notifications
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--incognito");
        options.addArguments("--disable-notifications");
        
        // Initialize WebDriver
        WebDriver driver = new ChromeDriver(options);
        
        try {
            // Open the URL
            driver.get("https://practicetestautomation.com/practice-test-login/");
            // Wait for 5 seconds
            Thread.sleep(5000);

            // Maximize the page
            driver.manage().window().maximize();

            // Wait for elements to appear
            driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

            // Perform login actions
            WebElement usernameField = driver.findElement(By.xpath("//input[@name='username']"));
            Thread.sleep(3000); // wait for 3 secs before action
            usernameField.sendKeys("student");

            WebElement passwordField = driver.findElement(By.xpath("//input[@name='password']"));
            Thread.sleep(3000); // wait for 3 secs before action
            passwordField.sendKeys("Password123");

            WebElement submitButton = driver.findElement(By.xpath("//button[@type='submit']"));
            Thread.sleep(3000); // wait for 3 secs before action
            submitButton.click();

            // Verify successful login
            Thread.sleep(3000); // wait for 3 secs before action
            WebElement logoutButton = driver.findElement(By.xpath("//a[text()='Log out']"));
            if (logoutButton.isDisplayed()) {
                System.out.println("Login test passed!");
                System.exit(0);
            } else {
                System.out.println("Login test failed!");
                System.exit(1);
            }

        } catch (Exception e) {
            System.out.println("An error occurred during the test execution.");
            System.exit(1);
        } finally {
            // Close the driver
            driver.quit();
        }
    }
}
