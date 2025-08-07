from weather_forcast_brain import WeatherBrain
from data import weather_data

# initalize weather forcast notificator
weather_notification = WeatherBrain(data=weather_data)

# run function to send message
weather_notification.send_message_about_rain()
