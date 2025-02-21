
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.util.concurrent.TimeUnit;

public class TestLoginInvoice {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless", "--disable-notifications", "--incognito");
        
        WebDriver driver = new ChromeDriver(options);

        try {
            driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
            driver.manage().window().maximize();

            driver.get("https://your-cep-portal-url"); // Replace with actual URL
            Thread.sleep(5000);

            WebDriverWait wait = new WebDriverWait(driver, 10);

            WebElement username = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@id='okta-signin-username']")));
            WebElement password = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@id='okta-signin-password']")));
            WebElement loginButton = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@id='okta-signin-submit']")));

            username.sendKeys("FRauto_beta1");
            Thread.sleep(3000);

            password.sendKeys("1@Loveingram12");
            Thread.sleep(3000);

            loginButton.click();
            Thread.sleep(3000);

            WebElement businessIcon = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//div[2]/div[1]/svg[@class~='MuiSvgIcon-fontSizeMedium MuiSvgIcon-root']")));
            businessIcon.click();
            Thread.sleep(3000);

            WebElement invoiceLink = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//span[text()='Mes factures / Mes avoirs']")));
            invoiceLink.click();
            Thread.sleep(3000);

            WebElement searchField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html//input[@id=':r4v:']")));
            searchField.sendKeys("217178006");
            Thread.sleep(3000);

            WebElement searchIcon = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//button[@aria-label='Search']"))); // Adjust locator as needed
            searchIcon.click();
            Thread.sleep(3000);

            // Check for search result validity
            boolean isResultValid = driver.findElements(By.xpath("//desired/locator/for/results")).size() > 0; // Adjust locator as needed

            if (isResultValid) {
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
