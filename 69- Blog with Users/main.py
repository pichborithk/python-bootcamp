import os
from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import login_user, LoginManager, current_user, logout_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()

from db import db, BlogPost, User, Comment
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap5(app)
# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_PATH")
db.init_app(app)

with app.app_context():
    db.create_all()


gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id, description="Invalid Information")


# Create admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


# Use Werkzeug to hash the user's password when creating a new user.
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        user_ = db.session.query(User).filter_by(email=email).first()

        if user_:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))

        hashed_password = generate_password_hash(
            password=form.password.data, method="pbkdf2:sha256", salt_length=8
        )
        new_user = User(email=email, password=hashed_password, name=form.name.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for("get_all_posts"))

    return render_template("register.html", form=form, current_user=current_user)


# Retrieve a user from the database based on their email.
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_ = db.session.query(User).filter_by(email=email).first()

        if not user_:
            flash("That email does not exist, please try again.")
            return redirect(url_for("login"))

        if not check_password_hash(user_.password, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))
        else:
            login_user(user_)
            return redirect(url_for("get_all_posts"))

    return render_template("login.html", form=form, current_user=current_user)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


# Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post,
        )
        db.session.add(new_comment)
        db.session.commit()
        comment_form.comment_text.data = ""

    return render_template(
        "post.html", post=requested_post, form=comment_form, current_user=current_user
    )


# Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form, current_user=current_user)


# Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template(
        "make-post.html", form=edit_form, is_edit=True, current_user=current_user
    )


# Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


# Error Handler
@app.errorhandler(404)
def invalid_route(e):
    return f"<h1>{e.name}</h1><p>{e.description}</p>", 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
