
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;
import java.util.logging.Level;
import java.util.logging.Logger;

public class LoginTest {

    private WebDriver driver;
    private final static Logger LOGGER = Logger.getLogger(LoginTest.class.getName());

    @BeforeClass
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--disable-notifications");
        options.addArguments("--incognito");
        driver = new ChromeDriver(options);

        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        driver.manage().window().maximize();
    }

    @Test
    public void testLogin() throws InterruptedException {
        try {
            LOGGER.info("Opening URL...");
            driver.get("https://practicetestautomation.com/practice-test-login/");
            Thread.sleep(5000);

            LOGGER.info("Entering username...");
            WebElement usernameField = driver.findElement(By.xpath("//input[@name='username']"));
            usernameField.sendKeys("student");
            Thread.sleep(3000);

            LOGGER.info("Entering password...");
            WebElement passwordField = driver.findElement(By.xpath("//input[@name='password']"));
            passwordField.sendKeys("Password123");
            Thread.sleep(3000);

            LOGGER.info("Clicking submit...");
            WebElement submitButton = driver.findElement(By.xpath("//button[@type='submit']"));
            submitButton.click();
            Thread.sleep(3000);

            LOGGER.info("Verifying successful login...");
            WebElement logoutButton = driver.findElement(By.xpath("//button[text()='Log out']"));
            Assert.assertTrue(logoutButton.isDisplayed(), "Log out button is not visible");
            LOGGER.info("Test case passed.");
        } catch (AssertionError e) {
            LOGGER.log(Level.SEVERE, "Assertion failed: " + e.getMessage());
            System.exit(1);
        } catch (Exception e) {
            LOGGER.log(Level.SEVERE, "Exception occurred: " + e.getMessage());
            System.exit(1);
        }
    }

    @AfterClass
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
        System.exit(0);
    }
}
