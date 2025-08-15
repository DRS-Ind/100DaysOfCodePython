from twilio.rest import Client


class NotificationManager:
    def __init__(self, api_sid: str, api_token: str, sender: str, verified_phone: str) -> None:
        """
        This class is responsible for talking to the Twilio API.

        :param api_sid: your Twilio API SID
        :param api_token:  your Twilio API token
        :param sender: your Twilio tel number
        :param verified_phone: your client number
        """
        self.sender = sender
        self.verified_phone = verified_phone
        self.client = Client(api_sid, api_token)

    def send_the_message_if_price_lowest(self, message: str) -> None:
        """
        The function sends a message to the sender

        :param message: message body to send
        """
        self.client.messages.create(from_=self.sender, body=message, to=self.verified_phone)
