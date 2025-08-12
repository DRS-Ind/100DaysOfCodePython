import requests
import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, api: str, secret: str) -> None:
        self._api = api
        self._secret = secret
        self._token = self._get_new_token()["access_token"]
        self.url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.headers = {"Authorization": f"Bearer {self._token}"}

    def _get_new_token(self) -> dict:
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api,
            'client_secret': self._secret
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)

        return response.json()

    def get_the_iata_code(self, sheet_data: list) -> list:
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        result = list()
        for row in sheet_data:
            params = {"keyword": row["city"]}
            response = requests.get(url=url, params=params, headers=self.headers).json()
            if response.get("warnings") is not None:
                row['iataCode'] = 'Not found'
            else:
                row['iataCode'] = response["data"][0]["iataCode"]
            result.append(row)
        return result

    def get_prices(self, data: list) -> list | None:
        result = list()
        for row in data:
            print(f"Get flight for {row["city"]}")
            params = {
                "originLocationCode": "LON",
                "destinationLocationCode": row["iataCode"],
                "departureDate": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
                "returnDate": (datetime.datetime.now() + datetime.timedelta(days=181)).strftime("%Y-%m-%d"),
                "adults": 1,
                "nonStop": "true",
                "currencyCode": "GBP"
            }
            response = requests.get(url=self.url, params=params, headers=self.headers)
            print(response.json())
            if response.status_code != 200:
                print(response.json())
                continue
            result.append(response.json())
        return result
