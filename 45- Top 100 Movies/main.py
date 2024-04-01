from bs4 import BeautifulSoup
import requests

# response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

# movies_el = soup.find_all(name="h3", class_="title")
movies_el = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

titles = [movie.getText() for movie in movies_el]

titles.reverse()

with open("movies.txt", mode="w") as file:
    for movie in titles:
        file.write(f"{movie}\n")