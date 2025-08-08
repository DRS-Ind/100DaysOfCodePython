from twilio.rest import Client
from credentials import twilio_sid, twilio_token, sender_phone, self_phone, STOCK


class DetectorBrain:
    def __init__(self, stock_data: dict, news_data: dict) -> None:
        """
        Back-end for stock change notifier.

        :param stock_data: dictionary with stock information
        :param news_data: dictionary with news
        """
        self.stock_data = stock_data
        self.news_data = news_data
        self.twilio_client = Client(twilio_sid, twilio_token)
        self.sender_phone = sender_phone
        self.self_phone = self_phone

    def get_stock_prices_for_two_days(self) -> list[float]:
        """
        The function parses stock information.

        :return: a list with 2 stock prices
        """
        return [float(value["4. close"]) for value in self.stock_data.values()][:2]

    def is_decrease(self) -> bool:
        """
        The function checks if the stock price decreases.

        :return: True if it does, False if it doesn`t
        """
        if self.get_stock_prices_for_two_days()[0] > self.get_stock_prices_for_two_days()[1]:
            return False
        return True

    def get_percent_diff_in_stock_prices(self) -> float:
        """
        Calculate the percentage difference between yesterday's stock price and the stock price before yesterday.

        :return: float number rounded to 2 symbols after the comma
        """
        two_last_day = self.get_stock_prices_for_two_days()
        percent = ((two_last_day[0] - two_last_day[1]) / two_last_day[1]) * 100
        return abs(round(percent, 1))

    def get_news(self) -> list:
        """
        Prepare news related to the stocks.

        :return: list with 3 str elements
        """
        return [(f"{STOCK}: {'🔻' if self.is_decrease() else '🔺'}{self.get_percent_diff_in_stock_prices()}%\n"
                 f"Headline: {news['title']}. \n"
                 f"Brief: {news['description']}.") for news in self.news_data]

    def send_message_about_diff_stock_prices(self) -> None:
        """
        The function will send a notification about a significant change in the stock price.
        """
        if self.get_percent_diff_in_stock_prices() > 5:
            for message in self.get_news():
                # for testing, doesn`t send messages from Twilio, prints messages in the command line
                print(message)
                self.twilio_client.messages.create(
                    body=message,
                    from_=self.sender_phone,
                    to=self.self_phone,
                )
