import dotenv

dotenv.load_dotenv()

from flask import Flask, render_template, request
import smtplib
import os

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")


from post import PostManager

app = Flask(__name__)

post_manager = PostManager()


@app.route("/")
def home():
    return render_template("index.html", posts=post_manager.posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:New Message\n\nName: {data['username']}\nEmail: {data['email']}\n"
                    f"Phone: {data['phone']}\nMessage:{data['message']}",
            )

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


@app.route("/posts/<int:post_id>")
def get_post(post_id):
    post = post_manager.get_post(post_id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
