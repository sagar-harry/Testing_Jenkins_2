
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class UIInvoiceSearchTest {

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--disable-notifications");
        options.addArguments("--incognito");
        WebDriver driver = new ChromeDriver(options);

        try {
            driver.manage().window().maximize();
            driver.get("https://your-cep-portal-url.com");

            Thread.sleep(5000);  // Wait for 5 secs after opening the page

            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

            // Wait and find username input
            WebElement usernameField = wait
                    .until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@id='okta-signin-username']")));
            Thread.sleep(3000);  // Wait for 3 secs before every action
            usernameField.sendKeys("FRauto_beta1");

            // Wait and find password input
            WebElement passwordField = wait
                    .until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@id='okta-signin-password']")));
            Thread.sleep(3000);  // Wait for 3 secs before every action
            passwordField.sendKeys("1@Loveingram12");

            // Wait and click login button
            WebElement loginButton = wait
                    .until(ExpectedConditions.elementToBeClickable(By.xpath("//input[@id='okta-signin-submit']")));
            Thread.sleep(3000);  // Wait for 3 secs before every action
            loginButton.click();

            // Wait and navigate to My Business
            WebElement businessIcon = wait
                    .until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//div[2]/div[1]/svg[contains(@class, 'MuiSvgIcon-fontSizeMedium')]")));
            Thread.sleep(3000);  // Wait for 3 secs before every action
            businessIcon.click();

            // Wait and go to Invoices
            WebElement invoiceLink = wait
                    .until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//?/span[@innertext='Mes factures / Mes avoirs']")));
            Thread.sleep(3000);  // Wait for 3 secs before every action
            invoiceLink.click();

            // Wait and input invoice number
            WebElement invoiceSearchField = wait
                    .until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/html//input[@id=':r4v:']")));
            Thread.sleep(3000);  // Wait for 3 secs before every action
            invoiceSearchField.sendKeys("217178006");

            // Wait and click search
            WebElement searchButton = wait
                    .until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//button[@id='search-icon']")));
            Thread.sleep(3000);  // Wait for 3 secs before every action
            searchButton.click();

            // Verify result
            boolean searchSuccess = wait.until(ExpectedConditions.textToBePresentInElementLocated(
                    By.xpath("//div[contains(text(), 'Search Results')]"), "217178006"));

            if (searchSuccess) {
                System.exit(0); // Test passed
            } else {
                System.exit(1); // Test failed
            }

        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1); // Test failed
        } finally {
            driver.quit();
        }
    }
}
