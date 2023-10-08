import os
import requests


class MovieAPI:
    TMDB_API_TOKEN = os.getenv("TMDB_API_TOKEN")
    HEADERS = {"Authorization": f"Bearer {TMDB_API_TOKEN}"}
    URL = "https://api.themoviedb.org/3"

    @staticmethod
    def search_movies(title):
        # can use API Key in PARAMS instead of TOKEN in HEADERS
        params = {"query": title}
        response = requests.get(
            url=f"{MovieAPI.URL}/search/movie",
            headers=MovieAPI.HEADERS,
            params=params,
        )
        data = response.json()
        return data["results"]

    @staticmethod
    def get_movie(movie_id):
        response = requests.get(
            f"{MovieAPI.URL}/movie/{movie_id}", headers=MovieAPI.HEADERS
        )
        data = response.json()
        return data
