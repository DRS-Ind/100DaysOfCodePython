import requests
import datetime
from user import PixelaUser


class GraphPixela:
    def __init__(self, user_info: PixelaUser, graph_id: str) -> None:
        """
        The class for operating user`s graphs in Pixela.

        :param user_info: PixelaUser class for information about user
        """
        self.user = user_info
        self.graph_id = graph_id
        self.graph_url = "/".join([user_info.url, user_info.username, "graphs"])

        self.header = {"X-USER-TOKEN": self.user.user_token}

    def create_graph(self, graph_name: str, graph_unit: str, graph_type: str, color: str) -> None:
        """
        The function creates a user`s graph on Pixela.

        :param graph_name: a name for your graph
        :param graph_unit: name a unit for your pixel grid
        :param graph_type: name a type of the unit
        :param color: set a color for your graph
        """
        params = {
            "id": self.graph_id,
            "name": graph_name,
            "unit": graph_unit,
            "type": graph_type,
            "color": color
        }

        requests.post(url=self.graph_url, json=params, headers=self.header)

    def add_checkmark_to_graph(self, quantity: int | float) -> None:
        """
        Set a checkmark with the right quantity today.

        :param quantity: quantity of the unit
        """
        url = "/".join([self.graph_url, self.graph_id])
        params = {
            "date": datetime.datetime.now().strftime("%Y%m%d"),
            "quantity": str(quantity)
        }

        requests.post(url=url, json=params, headers=self.header)

    def add_another_day_checkmark_to_graph(self, quantity: int | float, date: str) -> None:
        """
        Set a checkmark with the right quantity on a specific day.

        :param quantity: quantity of the unit
        :param date: date of the checkmark
        """
        url = "/".join([self.graph_url, self.graph_id])
        params = {
            "date": date,
            "quantity": str(quantity)
        }

        requests.post(url=url, json=params, headers=self.header)

    def update_checkmark(self, date: str, new_quantity: str) -> None:
        """
        Update the checkmark with the new quantity on a specific date.

        :param date: date of the checkmark
        :param new_quantity: new quantity of the unit
        """
        url = "/".join([self.graph_url, self.graph_id, date])
        params = {
            "quantity": new_quantity
        }

        requests.put(url=url, json=params, headers=self.header)
