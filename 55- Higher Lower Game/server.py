from flask import Flask
import random

app = Flask(__name__)

chosen_number = random.randint(0, 9)


@app.route("/")
def home():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'
    )


@app.route("/<int:n>")
def guess_number(n):
    if n < chosen_number:
        return ("<h1>It's too low</h1>"
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>')
    elif n > chosen_number:
        return ("<h1>It's too high</h1>"
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>')
    else:
        return ("<h1>You found me</h1>"
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>')


if __name__ == "__main__":
    app.run(debug=True)
