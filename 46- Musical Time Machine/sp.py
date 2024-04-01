from dotenv import load_dotenv

load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


class SP:
    CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
    USERNAME = os.getenv("SPOTIFY_USERNAME")

    def __init__(self):
        self.client = spotipy.Spotify(auth_manager=SP.get_oauth())
        self.user_id = self.client.current_user()["id"]

    def get_song_uri(self, song, year):
        result = self.client.search(q=f"track:{song} year:{year}", type="track")
        # print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
            return ""
        else:
            return uri

    def create_playlist(self, date, list_uris):
        playlist = self.client.user_playlist_create(
            user=self.user_id, name=f"{date} Billboard 100", public=False
        )
        self.client.playlist_add_items(playlist_id=playlist["id"], items=list_uris)
        print("Success create playlist")

    @staticmethod
    def get_oauth():
        return SpotifyOAuth(
            client_id=SP.CLIENT_ID,
            client_secret=SP.CLIENT_SECRET,
            redirect_uri=SP.REDIRECT_URI,
            scope="playlist-modify-private",
            show_dialog=True,
            cache_path="token.txt",
            username=SP.USERNAME,
        )
