#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv


if __name__ == '__main__':
    # load the variables from environment
    load_dotenv()

    FLIGHT_API_KEY = os.environ["FLIGHT_API_KEY"]
    FLIGHT_API_SECRET = os.environ["FLIGHT_API_SECRET"]
    SHEETY_API = os.environ["SHEETY_API"]
    TWILIO_SID = os.environ["TWILIO_SID"]
    TWILIO_TOKEN = os.environ["TWILIO_TOKEN"]
    SENDER_PHONE = os.environ["SENDER_PHONE"]
    VERIFIED_PHONE = os.environ["VERIFIED_PHONE"]

    # initialize main classes
    sheety_engine = DataManager(sheety_token=SHEETY_API)
    search_engine = FlightSearch(api=FLIGHT_API_KEY, secret=FLIGHT_API_SECRET)
    flight_data = FlightData()
    notifier_agent = NotificationManager(
        api_sid=TWILIO_SID,
        api_token=TWILIO_TOKEN,
        sender=SENDER_PHONE,
        verified_phone=VERIFIED_PHONE
    )

    print("Get info from sheets")
    data_from_sheets = sheety_engine.get_rows()

    # read information from sheets and update the iata codes if that column empty
    if data_from_sheets[0]["iataCode"] == "":
        print("Update sheets")
        updated_data = search_engine.get_the_iata_code(sheet_data=sheety_engine.get_rows())
        sheety_engine.update_city_codes(sheet_data=updated_data)
        data_from_sheets = sheety_engine.get_rows()

    print("Get flight prices")
    deals_data = search_engine.get_prices(data=data_from_sheets)

    print("Finding the cheapest one")
    flight_data.find_cheapest_flight(data=deals_data)

    # send message with the lowest prices if deal has it
    right_row = [row for row in data_from_sheets if flight_data.destination in row][0]
    if right_row["lowestPrise"] > flight_data.price:
        print(flight_data)
        notifier_agent.send_the_message_if_price_lowest(message=str(flight_data))
