from dotenv import load_dotenv

load_dotenv()
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


# Can set environment variable FLASH_APP equal to file name
# or use the code below to run flask app
# if __name__ == "__main__":
#     app.run()
