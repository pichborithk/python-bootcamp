import requests


class Post:
    def __init__(
        self, post_id, title, subtitle, body, date, author, image_alt, image_url
    ):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.date = date
        self.author = author
        self.image_alt = image_alt
        self.image_url = image_url


class PostManager:
    def __init__(self):
        self.posts = []
        self.get_all_posts()

    def get_post(self, post_id):
        return [post for post in self.posts if post.id == post_id][0]

    def get_all_posts(self):
        response = requests.get(url="https://api.npoint.io/eb6cd8a5d783f501ee7d")
        posts = response.json()
        for post in posts:
            post_obj = Post(
                post_id=post["id"],
                title=post["title"],
                subtitle=post["subtitle"],
                body=post["body"],
                date=post["date"],
                image_alt=post["image_alt"],
                author=post["author"],
                image_url=post["image_url"]
            )
            self.posts.append(post_obj)
