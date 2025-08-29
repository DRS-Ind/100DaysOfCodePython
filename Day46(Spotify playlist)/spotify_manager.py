import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


class SpotifyManager:
    def __init__(self, date) -> None:
        """
        The manager responsible for the connection with Spotify.
        
        :param date: valid date
        """
        self.year = date
        self.sp_client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"))
        self.sp_user_id = self.sp_client.current_user()["id"]
        self.sp_playlist_id = self.create_a_playlist()["id"]

    def get_songs_uri_from_list(self, song_names: list) -> list:
        """
        The function adds the Spotify URI to the list

        :param song_names: list with song names
        :return: list with Spotify URIs
        """
        result = list()
        for song in song_names:
            song_url = self.search_spotify_uri_name(song_name=song)
            if song_url is not None:
                result.append(song_url)
        return result

    def search_spotify_uri_name(self, song_name: str) -> str | None:
        """
        The function searches Spotify URI by song name.

        :param song_name: name of the song
        :return: Spotify URI
        """
        try:
            result = self.sp_client.search(q=f"track: {song_name} year: {self.year}", limit=1, type="track")["tracks"]
            song_uri = result["items"][0]["uri"]
        except IndexError:
            return None
        else:
            return song_uri

    def create_a_playlist(self) -> dict:
        """
        The function creates a Spotify playlist.

        :return: response from the api
        """
        return self.sp_client.user_playlist_create(
            user=self.sp_user_id,
            name=f"{self.year} Billboard 100",
            public=False
        )

    def add_songs_to_playlist(self, song_list: list) -> None:
        """
        The function adds songs to the playlist.

        :param song_list: list with Spotify URIs
        """
        self.sp_client.playlist_add_items(playlist_id=self.sp_playlist_id, items=song_list)