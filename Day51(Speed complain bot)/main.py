import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


# get sensitive information from .env file
load_dotenv()
PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 10


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        """
        The function measures internet speed and sends an X/Twitter complaint if the speed is less than promised.
        """
        self.x_url = "https://x.com/i/flow/login"
        self.speed_url = "https://www.speedtest.net/"


    @staticmethod
    def _setup_webdriver() -> WebDriver:
        """
        The function creates and sets up Selenium WebDriver.

        :return: Selenium WebDriver
        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()  # open window in full-size

        return driver

    def get_internet_speed(self) -> tuple[float, float]:
        """
        The function gets your current download and upload speed.

        :return: tuple with download and upload speed
        """
        driver = self._setup_webdriver()
        driver.get(url=self.speed_url)

        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "start-text").click()

        time.sleep(40)
        d_speed, u_speed = driver.find_elements(By.CLASS_NAME, value="result-data-large")
        d_speed, u_speed = float(d_speed.text), float(u_speed.text)

        driver.close()

        return d_speed, u_speed

    def tweet_at_provider(self, message: str) -> None:
        """
        The function sends the message/tweet to the x/twitter.
        """
        driver = self._setup_webdriver()
        driver.get(url=self.x_url)
        wait = WebDriverWait(driver=driver, timeout=2)

        # found a login field, clear it and enter your login
        login_box = wait.until(ec.presence_of_element_located((
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]'
                  '/div/div/div/div[4]/label/div/div[2]/div/input')))
        login_box.clear()
        login_box.send_keys(os.environ["X_LOGIN"], Keys.ENTER)

        # check request about x/twitter name
        try:
            verify = wait.until(ec.presence_of_element_located((
                By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]'
                '/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
            verify.send_keys(os.environ["X_NAME"], Keys.ENTER)
        except TimeoutException:
            pass

        # found a password field, clear it and enter your login
        pass_box = wait.until(ec.presence_of_element_located((
            By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]'
                  '/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        pass_box.clear()
        pass_box.send_keys(os.environ["X_PASS"], Keys.ENTER)

        # wait 5 seconds, then send the tweet
        time.sleep(5)
        tweet_box = driver.find_element(
            by=By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]'
                  '/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]'
                  '/div/div/div/div/div/div[2]/div/div/div/div'
        )
        tweet_box.clear()
        tweet_box.send_keys(message)
        tweet_btn = driver.find_element(
            by=By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]'
                  '/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span'
        )
        tweet_btn.click()


if __name__ == '__main__':
    # initialize SpeedBot and check internet speed
    bot = InternetSpeedTwitterBot()
    download, upload = bot.get_internet_speed()

    # if internet speed is less than promised, send a tweet
    if download < PROMISED_DOWNLOAD or upload < PROMISED_UPLOAD:
        tweet = (f" Hey Internet Provider, why is my internet speed {download}down/{upload}up "
                 f"when I pay for {PROMISED_DOWNLOAD}down/{PROMISED_UPLOAD}up?")
        bot.tweet_at_provider(message=tweet)
