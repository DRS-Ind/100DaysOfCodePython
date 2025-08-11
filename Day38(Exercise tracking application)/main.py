from brain import TrackerBrain
from credentials import nutrition_id, nutrition_api, sheety_token


if __name__ == '__main__':
    # initialise the app and give your credentials
    app = TrackerBrain(app_api_token=nutrition_api, app_id=nutrition_id, sheety_token=sheety_token)
    user_query = input("What do you do today? ")

    # save the response from nutrition
    app_response = app.get_info_about_exercises(text=user_query)

    # save new rows to the sheets
    app.add_rows_to_sheets(info=app_response)
