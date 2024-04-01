import requests
from bs4 import BeautifulSoup


class SongsManager:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get(cls):
        date = input(
            "Which year do you want to travel to? Tpe the date in the this format YYYY-MM-DD: "
        )
        return cls(date)

    @property
    def year(self):
        return self.date.split("-")[0]

    def get_titles(self):
        response = requests.get(
            url=f"https://www.billboard.com/charts/hot-100/{self.date}"
        )
        soup = BeautifulSoup(response.text, "html.parser")
        songs = soup.select("li ul li h3.c-title")
        # print(songs)
        return [song.getText().strip() for song in songs]
