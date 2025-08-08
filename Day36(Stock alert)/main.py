from data import stock_data, news_data
from detector_brain import DetectorBrain


if __name__ == '__main__':
    stock_notifier = DetectorBrain(stock_data=stock_data, news_data=news_data)

    stock_notifier.send_message_about_diff_stock_prices()
