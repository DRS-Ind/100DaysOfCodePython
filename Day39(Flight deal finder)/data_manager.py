import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheety_token: str) -> None:
        self.url = "https://api.sheety.co/b569962165298ea22bd827dad0637e83/flightDeals/prices"
        self.headers = {"Authorization": f"Bearer {sheety_token}"}

    def get_rows(self) -> list:
        return requests.get(url=self.url, headers=self.headers).json()["prices"]

    def update_city_codes(self, sheet_data: list):
        for row in sheet_data:
            row = {
                "price": row
            }
            requests.put(url=self.url + f"/{row["price"]["id"]}", json=row, headers=self.headers)
