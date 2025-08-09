import requests


class PixelaUser:
    def __init__(self, token: str, name: str) -> None:
        """
        The class for operating with Pixela user.

        :param token: user token from Pixela
        :param name: username from Pixela
        """
        self.user_token = token
        self.username = name
        self.url = "https://pixe.la/v1/users"

    def create_user(self) -> None:
        """
        Create a user on Pixela site.
        """
        params = {
            "token": self.user_token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }

        requests.post(url=self.url, json=params)

    def delete_user(self) -> None:
        """
        Delete a user on Pixela site.
        """
        requests.delete(url="/".join([self.url, self.username]))
