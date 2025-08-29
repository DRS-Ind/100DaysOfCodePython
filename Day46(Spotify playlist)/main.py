import datetime
from parser_manager import BillboardParser
from spotify_manager import SpotifyManager


if __name__ == '__main__':
    # verify if the user date exist in this reality
    try:
        date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        valid_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("This is not a valid date format.")
    else:
        # initialize managers
        parser = BillboardParser(year=date)
        sp = SpotifyManager(date=date)

        songs_data = parser.parse_site()
        songs = sp.get_songs_uri_from_list(song_names=songs_data)
        sp.add_songs_to_playlist(song_list=songs)
