
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import java.util.concurrent.TimeUnit;

public class CEPInvoiceTest {
    public static void main(String[] args) {
        // Set up ChromeOptions for headless, incognito, and disabling notifications
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        options.addArguments("--incognito");
        options.addArguments("--disable-notifications");
        
        // Initialize WebDriver
        WebDriver driver = new ChromeDriver(options);

        try {
            // Open CEP login page
            driver.get("https://login.example.com");
            TimeUnit.SECONDS.sleep(5); // Wait for 5 seconds

            // Maximize the window
            driver.manage().window().maximize();

            // Log in to the portal
            WebElement usernameField = driver.findElement(By.xpath("//input[@id='okta-signin-username']"));
            WebElement passwordField = driver.findElement(By.xpath("//input[@id='okta-signin-password']"));
            WebElement loginButton = driver.findElement(By.xpath("//input[@id='okta-signin-submit']"));

            usernameField.sendKeys("FRauto_beta1");
            TimeUnit.SECONDS.sleep(3); // Wait for 3 seconds
            passwordField.sendKeys("1@Loveingram12");
            TimeUnit.SECONDS.sleep(3); // Wait for 3 seconds
            loginButton.click();

            // Wait for elements to load
            TimeUnit.SECONDS.sleep(3); // Wait for 3 seconds
            
            // Navigate to invoices
            WebElement businessIcon = driver.findElement(By.xpath("//div[2]/div[1]/svg[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium']"));
            businessIcon.click();
            TimeUnit.SECONDS.sleep(3); // Wait for 3 seconds
            
            WebElement invoiceLink = driver.findElement(By.xpath("//*[@innertext='Mes factures / Mes avoirs']"));
            invoiceLink.click();

            // Wait for navigation to complete
            TimeUnit.SECONDS.sleep(3); // Wait for 3 seconds
            
            // Search for Invoice Number
            WebElement searchField = driver.findElement(By.xpath("/html//input[@id=':r4v:']"));
            WebElement searchButton = driver.findElement(By.cssSelector("searchButtonSelector")); // Assuming there is a placeholder here
            searchField.sendKeys("217178006");
            TimeUnit.SECONDS.sleep(3); // Wait for 3 seconds
            searchButton.click();

            // Validate search results
            boolean resultFound = driver.findElements(By.xpath("//expected/result/locator")).size() > 0;
            if (resultFound) {
                System.out.println("Test Passed");
                System.exit(0);
            } else {
                System.out.println("Test Failed");
                System.exit(1);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Test Failed");
            System.exit(1);
        } finally {
            // Cleanup
            driver.quit();
        }
    }
}
