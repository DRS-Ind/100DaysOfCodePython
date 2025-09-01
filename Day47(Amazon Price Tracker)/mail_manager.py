import os
import smtplib
import socket
from dotenv import load_dotenv

# load environment variables
load_dotenv()


class MailManager:
    def __init__(self) -> None:
        """
        The class is responsible for operating the mail.
        """
        self.__src_mail = os.environ["COMPANY_MAIL"]
        self.__src_pass = os.environ["COMPANY_MAIL_PASS"]
        self.target_mail = os.environ["TARGET_MAIL"]

    def send_message(self, message_body: str) -> None:
        """
        The function sends a message to the target email.

        :param message_body: message to send
        """
        if "gmail" in self.__src_mail:
            smtp_server = "smtp.gmail.com"
        elif "outlook" in self.__src_mail or "hotmail" in self.__src_mail:
            smtp_server = "smtp-mail.outlook.com"
        elif "yahoo" in self.__src_mail:
            smtp_server = "smtp.mail.yahoo.com"
        else:
            smtp_server = "Not in the list"  # fill what mail service you use
        try:
            with smtplib.SMTP(smtp_server) as connection:
                connection.starttls()
                connection.login(user=self.__src_mail, password=self.__src_pass)
                connection.sendmail(from_addr=self.__src_mail, to_addrs=self.target_mail,
                                    msg=f"Subject: Prices are down\n\n{message_body}")
        except (smtplib.SMTPException, socket.gaierror):
            print("Wrong smtp setting")
