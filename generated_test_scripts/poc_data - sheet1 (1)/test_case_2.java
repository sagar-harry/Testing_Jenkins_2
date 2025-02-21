
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.apache.log4j.Logger;

public class LoginPageTest {
    private WebDriver driver;
    private static final Logger logger = Logger.getLogger(LoginPageTest.class);

    @BeforeClass
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--disable-notifications");
        options.addArguments("--incognito");
        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
        logger.info("Browser maximized and running in headless incognito mode");
    }

    @Test
    public void testInvalidUsernameLogin() {
        try {
            driver.get("https://yourwebsite.com/login");
            Thread.sleep(5000);
            logger.info("Page opened");

            WebElement usernameField = waitForElement(By.xpath("//input[@name='username']"));
            usernameField.sendKeys("incorrectUser");
            logger.info("Entered invalid username");

            WebElement passwordField = waitForElement(By.xpath("//input[@name='password']"));
            passwordField.sendKeys("Password123");
            logger.info("Entered password");

            WebElement submitButton = waitForElement(By.xpath("//button[@type='submit']"));
            submitButton.click();
            logger.info("Submit button clicked");

            WebElement errorMessage = waitForElement(By.xpath("//div[contains(text(),'Invalid username')]"));
            Assert.assertTrue(errorMessage.isDisplayed(), "Error message is not displayed for invalid username");
            logger.info("Error message verified");

            System.exit(0);
        } catch (Exception e) {
            logger.error("Test failed", e);
            System.exit(1);
        }
    }

    private WebElement waitForElement(By locator) throws InterruptedException {
        for (int i = 0; i < 5; i++) {
            try {
                WebElement element = driver.findElement(locator);
                if (element.isDisplayed()) {
                    Thread.sleep(3000); // Wait for stability
                    return element;
                }
            } catch (Exception e) {
                Thread.sleep(1000);
            }
        }
        throw new RuntimeException("Element not found: " + locator.toString());
    }

    @AfterClass
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
