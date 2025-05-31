import random
import smtplib
import datetime as dt
# before using app, create credentials.py, with your information
from credentials import my_email, my_password, trgt_email


class MotivationSender:
    def __init__(self, target_email: str) -> None:
        self.__src_mail = my_email
        self.__src_pass = my_password
        self.target_email = target_email

    def send(self, subject: str, message: str) -> None:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.__src_mail, password=self.__src_pass)
            connection.sendmail(from_addr=self.__src_mail, to_addrs=self.target_email,
                                msg=f"Subject:{subject}\n\n{message}")

    def is_date_and_time(self) -> None:
        if dt.datetime.now().weekday() == 4:
            with open("quotes.txt", "r") as file:
                self.send(subject="Motivation", message=random.choice(file.readlines()))

if __name__ == "__main__":
    sender = MotivationSender(target_email=trgt_email)
    sender.is_date_and_time()
