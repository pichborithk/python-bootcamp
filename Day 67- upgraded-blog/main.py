import os
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_ckeditor import CKEditor
from datetime import date
from dotenv import load_dotenv

load_dotenv()

from db import db, BlogPost
from html_form import AddPostForm


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
Bootstrap5(app)
ckeditor = CKEditor(app)
# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_PATH")
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.query(BlogPost)
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route("/post/<int:post_id>")
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(
        BlogPost, post_id, description=f"Post with id: {post_id} does not exist."
    )
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = AddPostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    selected_post = db.get_or_404(
        BlogPost, post_id, description=f"Post with id: {post_id} does not exist."
    )
    form = AddPostForm(
        title=selected_post.title,
        subtitle=selected_post.subtitle,
        img_url=selected_post.img_url,
        author=selected_post.author,
        body=selected_post.body,
    )
    if form.validate_on_submit():
        selected_post.title = form.title.data
        selected_post.subtitle = form.subtitle.data
        selected_post.img_url = form.img_url.data
        selected_post.author = form.author.data
        selected_post.body = form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=selected_post.id))

    return render_template("make-post.html", form=form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(
        BlogPost, post_id, description=f"Post with id: {post_id} does not exist."
    )
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Error Handler
@app.errorhandler(404)
def invalid_route(e):
    return f"<h1>{e.name}</h1><p>{e.description}</p>", 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
