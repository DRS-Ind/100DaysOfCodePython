import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/b569962165298ea22bd827dad0637e83/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/b569962165298ea22bd827dad0637e83/flightDeals/users"


class DataManager:
    def __init__(self) -> None:
        """
        The class is responsible for speaking with the Sheety API.
        """
        self._token = os.environ["SHEETY_TOKEN"]
        self._headers = {"Authorization": f"Bearer {self._token}"}
        self.destination_data = {}

    def get_destination_data(self) -> dict:
        """
        The function uses the Sheety API to GET all the data in prices sheet.

        :returns: the data from prices sheet
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._headers)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        """
        The function makes a PUT request and use the row id from destination data to update the Google Sheet
        with the IATA codes.
        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=self._headers)

    def get_users_email(self) -> list:
        """
        The function uses the Sheety API to GET all the data in users sheet.
        """
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self._headers)
        return response.json()
