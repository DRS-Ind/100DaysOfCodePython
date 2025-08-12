from twilio.rest import Client


class NotificationManager:
    def __init__(self, api_sid: str, api_token: str, sender: str, verified_phone: str) -> None:
        self.sender = sender
        self.verified_phone = verified_phone
        self.client = Client(api_sid, api_token)

    def send_the_message_if_price_lowest(self, message: str) -> None:
        self.client.messages.create(from_=self.sender, body=message, to=self.verified_phone)
