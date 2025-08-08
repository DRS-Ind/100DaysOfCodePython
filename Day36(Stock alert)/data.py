import requests
from credentials import alpha_token, news_api_key, STOCK, COMPANY_NAME


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_token,
}
news_parameters = {
    "q": COMPANY_NAME,
    "from": "2025-08-05",
    "to": "2025-08-05",
    "apiKey": news_api_key
}

stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)

stock_response.raise_for_status()
news_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
news_data = news_response.json()["articles"][:3]
