from flask import Flask, render_template
from post import PostManager

app = Flask(__name__)

post_manager = PostManager()


@app.route("/")
def home():
    return render_template("index.html", posts=post_manager.posts)


@app.route("/posts/<int:post_id>")
def get_post(post_id):
    post = post_manager.get_post(post_id)
    return render_template("post.html", post=post)



if __name__ == "__main__":
    app.run(debug=True)
