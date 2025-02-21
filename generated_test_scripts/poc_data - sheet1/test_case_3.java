
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.WebElement;
import java.util.concurrent.TimeUnit;

public class UITest {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--disable-notifications");
        options.addArguments("--incognito");

        WebDriver driver = new ChromeDriver(options);

        try {
            driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

            driver.get("http://example.com");
            Thread.sleep(5000);

            driver.manage().window().maximize();

            Thread.sleep(3000);
            WebElement usernameField = driver.findElement(By.xpath("//input[@name='username']"));
            usernameField.sendKeys("student");

            Thread.sleep(3000);
            WebElement passwordField = driver.findElement(By.xpath("//input[@name='password']"));
            passwordField.sendKeys("incorrectPassword");

            Thread.sleep(3000);
            WebElement submitButton = driver.findElement(By.xpath("//button[@type='submit']"));
            submitButton.click();

            Thread.sleep(5000);

            WebElement errorMessage = driver.findElement(By.xpath("//*[contains(text(),'invalid password')]"));
            if (errorMessage.isDisplayed()) {
                System.exit(0);
            } else {
                System.exit(1);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        } finally {
            driver.quit();
        }
    }
}
