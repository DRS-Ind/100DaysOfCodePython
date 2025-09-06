import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec


def retry(func=None, retries=7, description=None):
    """
    The wrapper function for the redo action is useful for bad Ethernet connections.

    :param retries: retries count
    :param description: description for output
    """
    def decorator(func):
        def wrap(*args, **kwargs):
            for i_try in range(retries):
                print(f"Trying {description}. Attempt: {i_try + 1}")
                if func(*args, **kwargs):
                    return True
            return False

        return wrap
    time.sleep(2)

    # if using @retry without brackets
    if func:
        return decorator(func)
    return decorator



class RoutineAutomatizer:
    def __init__(self, email: str, password: str) -> None:
        """
        The class for booking gym classes

        :param email: email for login
        :param password: password for login
        """
        self.url = "https://appbrewery.github.io/gym/"
        self.__account_email = email
        self.__account_password = password
        self.driver = self.set_up_webdriver()
        self.wait = WebDriverWait(self.driver, 2)
        self.booked = 0
        self.waitlisted = 0
        self.already_in = 0
        self.detailed_class_list = ["\n--- DETAILED CLASS LIST ---"]

    def __str__(self) -> str:
        """
        The string interpretation of this class.
        :return: information about booked classes
        """
        return f"""\n--- BOOKING SUMMARY ---
Classes booked: {self.booked}
Waitlists joined: {self.waitlisted}
Already booked/waitlisted: {self.already_in}
Total Tuesday 6pm classes processed: {sum((self.booked, self.waitlisted, self.already_in))}"""

    def set_up_webdriver(self) -> WebDriver:
        """
        The function sets up Selenium Webdriver.

        :return: selenium webdriver
        """
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        options.add_argument(argument=f"--user-data-dir={user_data_dir}")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()  # open browser in full-window mode

        driver.get(url=self.url)

        return driver

    @retry(description="login")
    def login_in(self) -> bool:
        """
        The function logs in to the site.

        :return: True if success, False if not
        """
        login_button = self.wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

        email_box = self.wait.until(ec.presence_of_element_located((By.ID, "email-input")))
        email_box.clear()  # clear any information in the box
        email_box.send_keys(self.__account_email)

        password_box = self.driver.find_element(By.CSS_SELECTOR, value="#password-input")
        password_box.clear()  # clear any information in the box
        password_box.send_keys(self.__account_password)

        login_button = self.driver.find_element(By.CLASS_NAME, value="Login_submitButton__tJFna ")
        login_button.click()

        # check if you log in success
        try:
            self.wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
        except TimeoutException:
            return False
        else:
            return True

    def find_class(self) -> None:
        """
        The function search gym classes for book.
        """
        day_group = self.driver.find_elements(By.CSS_SELECTOR, 'div[id^="day-group-"]')
        # go through day cards
        for day in day_group:
            day_title = day.find_element(By.CSS_SELECTOR, 'h2[id^="day-title-"]').text
            # delete "Today" and "Tomorrow" from day_title if you don`t want those ones
            # if "(" in day_title or ")" in day_title:
            #     day_title = re.findall(r"\(([^)]+)\)", day_title)[0]

            # check if that`s a Tue or a Thu card
            if "Tue" in day_title or "Thu" in day_title:
                classes = day.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

                # iterate through classes
                for gym_class in classes:
                    class_time = gym_class.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

                    # find class on 6 PM
                    if "6:00 PM" in class_time:
                        btn = gym_class.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                        btn_name = btn.text.title()
                        class_name = gym_class.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
                        class_and_date = f"{class_name} on {day_title}"

                        # check the class and book if this one is not booked
                        if "ed" in btn_name:
                            self.already_in += 1
                            self.detailed_class_list.append(f"\t[Old {btn_name[:-2]}] {class_and_date}")
                            print(f"Already {btn_name}: {class_and_date}")
                        elif btn_name == "Join Waitlist":
                            self.book_class(btn)
                            self.waitlisted += 1
                            self.detailed_class_list.append(f"\t[New Waitlist] {class_and_date}")
                            print(f"Joined waitlist for: {class_and_date}")
                        elif btn_name == "Book Class":
                            self.book_class(btn)
                            self.booked += 1
                            self.detailed_class_list.append(f"\t[New Booking] {class_and_date}")
                            print(f"Successfully booked: {class_and_date}")
                        else:
                            pass

    @retry(description="book class")
    def book_class(self, button) -> bool:
        """
        The class booking feature.

        :param button: selenium web element
        :return: True if button pressed, False if not
        """
        try:
            button.click()
            self.wait.until(lambda _ : button.text == "Booked" or button.text == "Waitlisted")
        except TimeoutException:
            return False
        else:
            return True

    @retry(description="check booking")
    def go_my_booking(self) -> bool:
        """
        The function goes to the My Booking library.

        :return: True if successfully followed the link, False if not
        """
        try:
            self.driver.find_element(By.LINK_TEXT, value="My Bookings").click()
            self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "MyBookings_sectionTitle__XQq0G")))
        except TimeoutException:
            return False
        else:
            return True

    def verify_result(self) -> None:
        """
        The function gets information from "My booking" page.
        """
        # try to reach the page
        self.go_my_booking()

        # create a list of booked classes
        print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
        booking_and_waitlisting_list = (self.driver.find_elements(By.CSS_SELECTOR, value="h3[id^='booking-class-name-']") +
                        self.driver.find_elements(By.CSS_SELECTOR, value="h3[id^='waitlist-class-name-']"))
        for reserve in booking_and_waitlisting_list:
            print(f"\tVerified: {reserve.text}")

        # print verification result
        print("\n--- VERIFICATION RESULT ---")
        expected_num = len(self.detailed_class_list[:-1])
        found_num = len(booking_and_waitlisting_list)
        print(f"Expected: {expected_num} booking\nFound: {found_num} booking")
        if expected_num == found_num:
            print(f"SUCCESS: All bookings verified!")
        else:
            print(f"MISMATCH: Missing {abs(expected_num - found_num)} bookings")

if __name__ == '__main__':
    # fill the email and password class variable
    gym_manager = RoutineAutomatizer(email="__your_email__", password="__your_password__")
    if gym_manager.login_in():
        gym_manager.find_class()
        print(gym_manager)
        print("\n".join(gym_manager.detailed_class_list))
        gym_manager.verify_result()
        print("Success")
