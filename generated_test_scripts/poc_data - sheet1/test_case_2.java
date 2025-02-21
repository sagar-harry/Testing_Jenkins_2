
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class UITest {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--disable-notifications");
        options.addArguments("--incognito");
        
        WebDriver driver = new ChromeDriver(options);

        try {
            driver.manage().window().maximize();
            driver.get("http://yourwebsite.com");
            Thread.sleep(5000);

            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

            By usernameLocator = By.xpath("//input[@name='username']");
            By passwordLocator = By.xpath("//input[@name='password']");
            By submitButtonLocator = By.xpath("//button[@type='submit']");
            By errorMessageLocator = By.id("error-message-id"); // replace with the actual id

            wait.until(ExpectedConditions.visibilityOfElementLocated(usernameLocator));
            Thread.sleep(3000);
            WebElement usernameField = driver.findElement(usernameLocator);
            usernameField.sendKeys("incorrectUser");

            wait.until(ExpectedConditions.visibilityOfElementLocated(passwordLocator));
            Thread.sleep(3000);
            WebElement passwordField = driver.findElement(passwordLocator);
            passwordField.sendKeys("Password123");

            wait.until(ExpectedConditions.visibilityOfElementLocated(submitButtonLocator));
            Thread.sleep(3000);
            WebElement submitButton = driver.findElement(submitButtonLocator);
            submitButton.click();

            wait.until(ExpectedConditions.visibilityOfElementLocated(errorMessageLocator));
            Thread.sleep(3000);
            WebElement errorMessage = driver.findElement(errorMessageLocator);
            if (errorMessage.isDisplayed()) {
                System.out.println("Test Passed");
                System.exit(0);
            } else {
                System.out.println("Test Failed");
                System.exit(1);
            }

        } catch (Exception e) {
            System.out.println("Test Failed: " + e.getMessage());
            System.exit(1);
        } finally {
            driver.quit();
        }
    }
}
