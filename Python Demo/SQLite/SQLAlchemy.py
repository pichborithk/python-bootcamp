from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
db = SQLAlchemy()
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():  # we can ignore app_context() if we query database inside app.route etc...
    new_book = Books(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# READ RECORD
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    print(all_books)

with app.app_context():
    book = db.session.execute(
        db.select(Books).where(Books.title == "Harry Potter")
    ).scalar()
    print(book)

# UPDATE RECORD
with app.app_context():
    book_to_update = db.session.execute(
        db.select(Books).where(Books.title == "Harry Potter")
    ).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    # or book_to_update = db.one_or_404(db.select(Books).filter_by(title="Harry Potter"))
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# DELETE RECORD
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    # or book_to_delete = db.one_or_404(db.select(Books).filter_by(title="Harry Potter"))
    db.session.delete(book_to_delete)
    db.session.commit()
