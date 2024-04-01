from dotenv import load_dotenv

load_dotenv()
from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        text = func()
        return f"<b>{text}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route("/")
@make_bold
@make_underlined
@make_emphasis
def hello_world():
    return "Hello, World!"


@app.route("/<name>/<int:post_id>")
def greet(name, post_id):
    return f"<h1>Hello, {name} this is post number {post_id}"


@app.route("/path/<path:sub_path>")
def show_sub_path(sub_path):
    # show the sub path after /path/
    return f"Sub path {sub_path}"


# Can set environment variable FLASH_APP equal to file name
# or use the code below to run flask app
# if __name__ == "__main__":
#     app.run(debug=True)
