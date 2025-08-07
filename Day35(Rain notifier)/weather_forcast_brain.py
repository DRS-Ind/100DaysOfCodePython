from twilio.rest import Client
from credentials import twilio_sid, twilio_token, sender_phone, self_phone


class WeatherBrain:
    def __init__(self, data: list) -> None:
        """
        The program operates on data to send you a message about whether it'll be raining.

        :param data: data to operate
        """
        self.weather_data = data
        self.twilio_client = Client(twilio_sid, twilio_token)
        self.sender_phone = sender_phone
        self.self_phone = self_phone

    def is_raining_near_future(self) -> bool:
        """
        The function checks whether it'll be raining.

        :return: True if will, False if will not
        """
        for weather_situation in self.weather_data:
            if weather_situation["weather"][0]["id"] < 600:
                return True
        return False

    def send_message_about_rain(self) -> None:
        """
        The function will send a notification about the umbrella if it's going to rain today.
        """
        if self.is_raining_near_future():
            print("Send")
            self.twilio_client.messages.create(
                body="Візьми парасольку☔ з собою",
                from_=self.sender_phone,
                to=self.self_phone,
            )
