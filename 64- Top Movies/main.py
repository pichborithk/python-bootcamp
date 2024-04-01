import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv

load_dotenv()

from movie_api import MovieAPI
from html_form import EditMovieForm, SearchMovieForm
from db import db, Movies

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_PATH")
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditMovieForm()
    movie_id = request.args.get("movie_id")
    movie_selected = db.get_or_404(Movies, movie_id)
    if form.validate_on_submit():
        # movie_rating = request.form["rating"]
        movie_rating = form.rating.data
        # movie_review = request.form["review"]
        movie_review = form.review.data
        movie_selected.rating = movie_rating
        movie_selected.review = movie_review
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie_selected, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    movie_selected = db.get_or_404(Movies, movie_id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        all_movies = MovieAPI.search_movies(title=title)
        return render_template("select.html", movies=all_movies)

    return render_template("search.html", form=form)


@app.route("/add")
def add():
    movie_id = request.args.get("movie_id")
    data = MovieAPI.get_movie(movie_id=movie_id)
    new_movie = Movies(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        description=data["overview"],
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", movie_id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)
