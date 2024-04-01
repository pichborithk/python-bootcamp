import requests


class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body


class PostManager:
    def __init__(self):
        self.posts = []
        self.get_all_posts()

    def get_post(self, post_id):
        return [post for post in self.posts if post.id == post_id][0]

    def get_all_posts(self):
        response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
        posts = response.json()
        for post in posts:
            post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
            self.posts.append(post_obj)
