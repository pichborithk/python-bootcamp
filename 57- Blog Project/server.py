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


# @app.route("/guess/<name>")
# def guess(name):
#     response_agify = requests.get(url=f"https://api.agify.io?name={name}")
#     age = response_agify.json()["age"]
#     response_genderize = requests.get(url=f"https://api.genderize.io/?name={name}")
#     gender = response_genderize.json()["gender"]
#
#     return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
