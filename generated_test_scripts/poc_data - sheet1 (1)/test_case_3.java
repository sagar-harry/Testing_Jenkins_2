
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class LoginTest {
    private WebDriver driver;
    private WebDriverWait wait;
    private static final Logger logger = LogManager.getLogger(LoginTest.class);

    public static class LoginPage {
        WebDriver driver;
        
        By usernameField = By.xpath("//input[@name='username']");
        By passwordField = By.xpath("//input[@name='password']");
        By submitButton = By.xpath("//button[@type='submit']");
        
        public LoginPage(WebDriver driver) {
            this.driver = driver;
            PageFactory.initElements(driver, this);
        }
        
        public void enterUsername(String username) {
            waitUntilVisible(usernameField).sendKeys(username);
        }
        
        public void enterPassword(String password) {
            waitUntilVisible(passwordField).sendKeys(password);
        }
        
        public void clickSubmit() {
            waitUntilVisible(submitButton).click();
        }

        private WebElement waitUntilVisible(By locator) {
            return (new WebDriverWait(driver, 10)).until(ExpectedConditions.visibilityOfElementLocated(locator));
        }
    }

    @BeforeClass
    public void setup() {
        logger.info("Setting up the environment and driver");
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless", "--disable-notifications", "--incognito");
        driver = new ChromeDriver(options);
        wait = new WebDriverWait(driver, 10);
        
        driver.manage().window().maximize();
        logger.info("Navigating to the URL");
        driver.get("http://example.com/login");
        waitBeforeNextAction(5000);
    }

    @Test
    public void testInvalidPassword() {
        try {
            LoginPage loginPage = new LoginPage(driver);
            waitBeforeNextAction(3000);
            loginPage.enterUsername("student");
            waitBeforeNextAction(3000);
            loginPage.enterPassword("incorrectPassword");
            waitBeforeNextAction(3000);
            loginPage.clickSubmit();
            waitBeforeNextAction(3000);
            
            WebElement errorElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[contains(text(),'Invalid password')]")));
            Assert.assertNotNull(errorElement, "Error message should be displayed for invalid password");
            logger.info("Test case passed");
            System.exit(0);
        } catch (Exception e) {
            logger.error("Test case failed", e);
            System.exit(1);
        }
    }

    @AfterClass
    public void teardown() {
        logger.info("Closing the browser");
        if (driver != null) {
            driver.quit();
        }
    }

    private void waitBeforeNextAction(int milliseconds) {
        try {
            Thread.sleep(milliseconds);
        } catch (InterruptedException e) {
            logger.error("Interrupted Exception occurred", e);
        }
    }
}
