import requests


class DataManager:
    def __init__(self, sheety_token: str) -> None:
        """
        This class is responsible for talking to the Google Sheet.

        :param sheety_token: Your personal token for sheety account.
        """
        self.url = "https://api.sheety.co/b569962165298ea22bd827dad0637e83/flightDeals/prices"
        self.headers = {"Authorization": f"Bearer {sheety_token}"}

    def get_rows(self) -> list:
        """
        The function reads Google Sheets and returns a dict with an information from this one.
        """
        return requests.get(url=self.url, headers=self.headers).json()["prices"]

    def update_city_codes(self, sheet_data: list):
        """
        The function updates rows in Google Sheets.

        :param sheet_data: new rows
        """
        for row in sheet_data:
            row = {
                "price": row
            }
            requests.put(url=self.url + f"/{row["price"]["id"]}", json=row, headers=self.headers)
