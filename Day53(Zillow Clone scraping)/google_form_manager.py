from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class GFormManager:
    def __init__(self) -> None:
        """
        The class is responsible for communicating with Google Forms.
        """
        self.url = ("https://docs.google.com/forms/d/e/1FAIpQLSfFSR-APxyzRwkaXPnj46I4GQdY"
                    "3nyLla_SZJw2yPnUl2DoLg/viewform?usp=dialog")

    def send_info(self, hrefs: list, prices: list, addresses: list) -> None:
        """
        The function is filling up information in Google Forms.

        :param hrefs: list with links
        :param prices: list with prices
        :param addresses: list with addresses
        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        driver.get(url=self.url)

        wait = WebDriverWait(driver=driver, timeout=2)  # wait before filing

        for address, price, href in zip(addresses, prices, hrefs):
            address_box = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]'
                                                                               '/div[1]/div/div/div[2]/div/div[1]'
                                                                               '/div/div[1]/input')))
            address_box.click()  # click the text box
            address_box.clear()  # clear the box
            address_box.send_keys(address)  # fill the box

            price_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                      '/div/div[1]/div/div[1]/input')
            price_box.click()
            price_box.clear()
            price_box.send_keys(price)

            href_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                                     '/div/div[1]/div/div[1]/input')
            href_box.click()
            href_box.clear()
            href_box.send_keys(href)

            # click send
            driver.find_element(By.CLASS_NAME, "NPEfkd").click()

            # check if information is sent and prepare for sending another pack of information
            try:
                another_answer_btn = wait.until(ec.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                ))
                another_answer_btn.click()
            except TimeoutException:
                # else print error and stop sending information
                print("Error")
                break

