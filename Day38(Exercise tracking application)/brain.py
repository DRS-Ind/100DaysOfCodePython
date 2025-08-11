import requests
from datetime import datetime


class TrackerBrain:
    def __init__(self, app_api_token: str, app_id: str, sheety_token: str) -> None:
        """
        Exercise Tracking Application witch save your workout result to the Google Sheets.

        :param app_api_token: nutritionix api token
        :param app_id: nutritionix id
        :param sheety_token: sheety api token
        """
        self.token = app_api_token
        self.id = app_id
        self.sheety_token = sheety_token
        self.nutrition_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.sheety_url = "https://api.sheety.co/fc633c4a7c83a8cf04b353197e17e378/myWorkouts/workouts"

    def get_info_about_exercises(self, text: str) -> list:
        """
        The function gets information about your exercises using natural language.

        :param text: prompt about your activity
        :return: a list with information about exercises
        """
        params = {"query": text}
        headers = {
            "x-app-id": self.id,
            "x-app-key": self.token
        }
        return requests.post(url=self.nutrition_url, json=params, headers=headers).json()["exercises"]

    def add_rows_to_sheets(self, info: list) -> None:
        """
        The function creates the rows and saves them to Google Sheets.

        :param info: information to parse
        """
        for exercise in info:
            params = {
                "workout": {
                    "date": datetime.now().strftime("%d/%m/%Y"),
                    "time": datetime.now().strftime("%T"),
                    "exercise": exercise["name"].title(),
                    "duration": str(exercise["duration_min"]),
                    "calories": str(exercise["nf_calories"])
                }
            }
            headers = {"Authorization": f"Bearer {self.sheety_token}"}
            response = requests.post(url=self.sheety_url, json=params, headers=headers)
            response.raise_for_status()
