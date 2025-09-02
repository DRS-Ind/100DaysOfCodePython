import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By


class Clicker:
    def __init__(self) -> None:
        """
        The class is responsible for playing in Stimulation Clicker.
        """
        self.url = "https://neal.fun/stimulation-clicker/"
        self.driver = self.driver_setup()

    def driver_setup(self):
        """
        The function sets up Selenium WebDriver.

        :return: selenium webdriver
        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(url=self.url)

        return driver

    def click_and_upgrade(self) -> None:
        """
        The function starts the unstoppable click&upgrade sequence.
        """
        # find the button
        button = self.driver.find_element(By.CLASS_NAME, value='main-btn')

        # tap first 10 times before upgrades appear
        for _ in range(10):
            button.click()

        # start unstoppable click
        while 1:
            try:
                # find upgrade list
                upgrades = self.driver.find_elements(By.CSS_SELECTOR, value='.upgrade')
                for upgrade in upgrades[:-1]:
                    button.click()
                    upgrade.click()
            # pass if element is not clickable
            except selenium.common.exceptions.ElementClickInterceptedException:
                pass
            except selenium.common.exceptions.StaleElementReferenceException:
                pass


if __name__ == '__main__':
    # initialize clicker class
    clicker = Clicker()

    # start clicking
    clicker.click_and_upgrade()
