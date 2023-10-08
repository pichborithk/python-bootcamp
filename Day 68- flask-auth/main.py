import os
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
from dotenv import load_dotenv

load_dotenv()

from db import db, User

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_PATH")
db.init_app(app)
# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        hash_and_salted_password = generate_password_hash(
            request.form.get("password"), method="pbkdf2:sha256", salt_length=8
        )
        new_user = User(
            email=request.form.get("email"),
            name=request.form.get("name"),
            password=hash_and_salted_password,
        )

        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # Check stored password hash against entered password hashed.
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("secrets"))

    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    print(current_user.name)
    # Passing the name from the current_user
    return render_template("secrets.html", name=current_user.name)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


# Only logged-in users can down download the pdf
@app.route("/download")
@login_required
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
