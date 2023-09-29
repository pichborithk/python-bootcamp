from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# header = soup.find(name="h1", id="name")
# print(header)
#
# section_header = soup.find(name="h3", class_="heading")
# print(section_header)

# company_url = soup.select_one(selector="p a")
#
# section_header = soup.select(selector="h3 .heading")

response = requests.get(url="https://news.ycombinator.com")
soup = BeautifulSoup(response.text, "html.parser")

# articles = soup.find_all(name="a", class_="titleline")
articles = soup.select(selector=".titleline > a")
article_upvotes = soup.find_all(name="span", class_="score")

my_articles_list = []

for index in range(len(articles)):
    text = articles[index].getText()
    link = articles[index].get("href")
    try:
        upvote = int(article_upvotes[index].getText().split(" ")[0])
    except IndexError:
        upvote = 0
    my_articles_list.append({"title": text, "link": link, "upvote": upvote})


print(my_articles_list[0])

my_articles_sorted_list = sorted(
    my_articles_list, key=lambda article: article["upvote"], reverse=True
)
print(my_articles_sorted_list[0])
