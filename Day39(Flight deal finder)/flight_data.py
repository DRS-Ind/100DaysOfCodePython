from flight_search import FlightSearch
from data_manager import DataManager


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(
            self,
            price: float = None,
            origin: str = None,
            destination: str = None,
            out: str = None,
            return_date: str = None
    ) -> None:
        self.price = price
        self.origin = origin
        self.destination = destination
        self.out = out
        self.return_date = return_date

    def __str__(self) -> str:
        return (f"Low price alert! Only £{self.price} to fly from {self.origin} to {self.destination}, "
                f"on {self.out} until {self.return_date}.")

    def find_cheapest_flight(self, data) -> None:
        for deals in data:
            print(deals)
            for deal in deals["data"]:
                price = float(deal["price"]["grandTotal"])
                if self.price is None or self.price > price:
                    deal_data = {
                        "price": price,
                        "from": deal["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                        "to": deal["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                        "on": deal["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
                        "until": deal["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                    }
                    print(deal_data)
                    self.price, self.origin, self.destination, self.out, self.return_date = deal_data.values()
