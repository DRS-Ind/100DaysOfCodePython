##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import random
import socket
import pandas
import smtplib
import logging
import datetime as dt
from spicy_info import my_email, my_password  # before using app, create spicy_info.py, with your information


logging.basicConfig()


class BirthdayWisher:
    def __init__(self, birthday_file_location: str, folder_with_wishes: str) -> None:
        """
        The app sends birthday wishes to recipients which ones is today.

        :param birthday_file_location: location of .csv file with information about birthdays.
        :param folder_with_wishes: location of folder with .txt files with wishes inside.
        """
        self.__src_mail = my_email
        self.__src_pass = my_password
        self.birthday_data = pandas.read_csv(birthday_file_location)
        self.wishes_folder = folder_with_wishes

    def send(self, subject: str, message: str, target_mail: str) -> None:
        """
        The function send message to the target mail.
        :param subject: str value for mail`s subject
        :param message: str value for mail`s message
        :param target_mail: str value for target email
        """
        logging.info("Start sending message")
        if "gmail" in self.__src_mail:
            smtp_server = "smtp.gmail.com"
        elif "outlook" in self.__src_mail or "hotmail" in self.__src_mail:
            smtp_server = "smtp-mail.outlook.com"
        elif "yahoo" in self.__src_mail:
            smtp_server = "smtp.mail.yahoo.com"
        else:
            smtp_server = "Not in the list"  # fill what mail service you use
            logging.warning("smtp-server not found")
        try:
            with smtplib.SMTP(smtp_server) as connection:
                connection.starttls()
                connection.login(user=self.__src_mail, password=self.__src_pass)
                connection.sendmail(from_addr=self.__src_mail, to_addrs=target_mail,
                                    msg=f"Subject:{subject}\n\n{message}")
        except (smtplib.SMTPException, socket.gaierror):
            logging.warning("Wrong smtp setting")
        logging.info("Message sent")

    def is_right_day_and_time(self) -> pandas.DataFrame:
        """
        The function to find all today`s birthdays information
        :return: all information about birthdays today
        """
        logging.info("Start searching birthday")
        right_month = self.birthday_data.month == float(dt.datetime.now().month)
        right_day = self.birthday_data.day == float(dt.datetime.now().day)
        logging.info("Complete searching birthday")
        return self.birthday_data[right_month & right_day]

    def text_from_random_file(self, name: str) -> str | None:
        """
        The function to get info from a random text file in a folder
        :param name: name to replace
        :return: personal birthday wish
        """
        logging.info("Start parsing text files")
        files = os.listdir(self.wishes_folder)
        if files:
            random_file = random.choice(files)
            file_path = os.path.join(self.wishes_folder, random_file)
            with open(file_path, 'r') as file:
                contents = file.read()
                contents = contents.replace("[NAME]", name)
                logging.info("Complete parsing text")
                return contents
        else:
            logging.warning("The folder is empty")
            return None

    def main(self) -> None:
        """
        The main script to execute.
        """
        logging.info("Start app")
        data = self.is_right_day_and_time()
        if not data.empty:
            message_text = self.text_from_random_file(data.name.item())
            if message_text is not None:
                self.send(subject="Happy Birthday", message=message_text, target_mail=data.email)
                logging.info("Complete sending message")
            else:
                logging.warning("Message isn`t sent, message text is null")
        else:
            logging.warning("Message isn`t sent, birthday isn`t found")


if __name__ == "__main__":
    wisher = BirthdayWisher(birthday_file_location="birthdays.csv", folder_with_wishes="./letter_templates")
    wisher.main()
