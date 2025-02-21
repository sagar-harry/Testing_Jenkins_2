
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.util.concurrent.TimeUnit;

public class UITest {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--disable-notifications");
        options.addArguments("--disable-popup-blocking");
        options.addArguments("--incognito");

        WebDriver driver = new ChromeDriver(options);
        WebDriverWait wait = new WebDriverWait(driver, 10);

        try {
            driver.get("http://yourpageurl.com");
            driver.manage().window().maximize();
            TimeUnit.SECONDS.sleep(5);

            By usernameLocator = By.xpath("//input[@name='username']");
            By passwordLocator = By.xpath("//input[@name='password']");
            By submitButtonLocator = By.xpath("//button[@type='submit']");
            By errorMessageLocator = By.xpath("//*[contains(text(), 'invalid username')]");

            // Wait for elements to appear and interact
            wait.until(ExpectedConditions.visibilityOfElementLocated(usernameLocator));
            driver.findElement(usernameLocator).sendKeys("incorrectUser");
            TimeUnit.SECONDS.sleep(3);

            wait.until(ExpectedConditions.visibilityOfElementLocated(passwordLocator));
            driver.findElement(passwordLocator).sendKeys("Password123");
            TimeUnit.SECONDS.sleep(3);

            wait.until(ExpectedConditions.elementToBeClickable(submitButtonLocator));
            driver.findElement(submitButtonLocator).click();
            TimeUnit.SECONDS.sleep(3);

            // Verify error message for invalid username
            wait.until(ExpectedConditions.visibilityOfElementLocated(errorMessageLocator));
            WebElement errorMessage = driver.findElement(errorMessageLocator);

            if (errorMessage.isDisplayed()) {
                System.out.println("Test Passed: Error message is displayed.");
                System.exit(0);
            } else {
                System.out.println("Test Failed: Error message is not displayed.");
                System.exit(1);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Test Failed due to an Exception.");
            System.exit(1);
        } finally {
            driver.quit();
        }
    }
}
