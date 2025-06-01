import requests
from datetime import datetime


class MyISS:
    def __init__(self) -> None:
        """
        The app notify if the ISS can be seen near you.
        """
        self.my_lat = 80.981569
        self.my_lon = -51.1247
        self.iss_position_api_url = "http://api.open-notify.org/iss-now.json"
        self.sunset_sunrise_api_url = "https://api.sunrise-sunset.org/json"

    def get_iss_coordinates(self) -> dict:
        """
        The function to get coordinates of ISS.
        :return: dictionary with longitude and latitude
        """
        response = requests.get(url=self.iss_position_api_url)
        response.raise_for_status()
        return response.json()["iss_position"]

    def is_dark(self) -> bool:
        """
        The function checks if it's dark outside.
        :return: True if it's dark or False if it's bright
        """
        key_argument = {"lat": self.my_lat, "lng": self.my_lon, "formatted": 0}
        response = requests.get(url=self.sunset_sunrise_api_url, params=key_argument)
        response.raise_for_status()

        sunrise_time = response.json()["results"]["sunrise"][11:19].split(":")
        sunset_time = response.json()["results"]["sunset"][11:19].split(":")
        actual_time = str(datetime.now().timetz())[:-7].split(":")

        if sunset_time < actual_time or actual_time < sunrise_time:
            return True
        return False

    def start(self) -> None:
        """
        The main function for execution.
        """
        if self.is_dark():
            iss_lat, iss_lon = (float(value) for value in self.get_iss_coordinates().values())
            if self.my_lat - 5 < iss_lat < self.my_lat + 5 and self.my_lon - 5 < iss_lon < self.my_lon + 5:
                print("He`s upside")
            else:
                print("He`s not with us")


if __name__ == "__main__":
    my_iss = MyISS()
    my_iss.start()
