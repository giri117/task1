package edmodo.selenium.webdriver;

import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Edmodo {
	WebDriver driver;
	int hour, minute, second, millisecond;
	double current_time, recent_time = 0.0;
	
	public void CurrentTime(){
		GregorianCalendar time = new GregorianCalendar();
		hour = time.get(Calendar.HOUR);
		minute = time.get(Calendar.MINUTE);
		second = time.get(Calendar.SECOND);
		//System.out.println("Current time is :"+hour+":"+minute+":"+second+":"+millisecond);
		current_time = hour*3600+minute*60+second;
		System.out.println(current_time+";"+(current_time-recent_time));
		recent_time = current_time;
	}
	

	public void invokeBrowser(){
		try {
			///1
			CurrentTime();
			System.setProperty("webdriver.chrome.driver", "C:\\Users\\Krish\\Documents\\selenium\\chromedriver_win32\\chromedriver.exe");
			driver = new ChromeDriver();
			driver.manage().deleteAllCookies();
			driver.manage().window().maximize();
			driver.manage().timeouts().implicitlyWait(100, TimeUnit.SECONDS);
			driver.manage().timeouts().pageLoadTimeout(100, TimeUnit.SECONDS);
		    EdmodoTesting();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	
	}	
	public void EdmodoTesting(){
		try {
			///2
			CurrentTime();
			driver.get("https://www.edmodo.com/");
			
			CurrentTime();
			
			driver.findElement(By.id("qa-test-top-login-button")).click();
			///4
			CurrentTime();
			driver.findElement(By.id("un")).sendKeys("sai00898@gmail.com");
			driver.findElement(By.id("pw")).sendKeys("giri@writer6");
			driver.findElement(By.id("qa-test-lightbox-login")).click();
			///5
			CurrentTime();
			driver.findElement(By.xpath(".//*[@id='mainnav']/li[5]")).click();
			driver.findElement(By.xpath(".//*[@id='chats-landing-page']/div/div[2]/div/div/div/div/div/footer/div/div/form/textarea")).sendKeys("Did you submitted your Homework??");
			driver.findElement(By.xpath(".//*[@id='chats-landing-page']/div/div[2]/div/div/div/div/div/footer/div/div/form/div[4]/div/button")).click();
			driver.navigate().back();
			driver.navigate().back();
			///6
			CurrentTime();
			driver.findElement(By.xpath(".//*[@id='content']/div/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div/div/div[6]/div/div[2]/table/tbody/tr/td[2]/div/div/div[1]/textarea")).sendKeys("This is new Assignment");
			driver.findElement(By.xpath(".//*[@id='content']/div/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div[1]/div/div/div[6]/div/div[2]/table/tbody/tr/td[2]/div/div/div[3]/div[2]/button")).click();
			///7
			CurrentTime();
			driver.findElement(By.xpath(".//html/body/div[4]/div/div/div[2]/ul/li[7]/a[1]/span/i")).click();
			driver.findElement(By.xpath(".//html/body/div[4]/div/div/div[2]/ul/li[7]/div/ul/li[9]/a/span")).click();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Edmodo myObj = new Edmodo();
		myObj.invokeBrowser();
		
		
		

	}

}
