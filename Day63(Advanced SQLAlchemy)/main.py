import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, update
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, SubmitField, SelectField

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
# class for initialize SQLAlchemy
class Base(DeclarativeBase):
    pass

app = Flask(__name__)
db = SQLAlchemy(model_class=Base)

# connect database to the flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collections.db"
db.init_app(app)

class Books(db.Model):
    """
    The SQL table.
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


@app.context_processor
def now_html():
    """
    The function adds HTML content to the page.
    """
    current_time = datetime.datetime.now()
    return {"now": current_time}

@app.route('/')
def home():
    """
    The main page.
    """
    all_books = Books.query.all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    """
    The page for adding new book.
    """
    if request.method == "POST":
        # add new record to the table
        with app.app_context():
            new_book = Books(title=request.form.get("book_name"),
                             author=request.form.get("book_author"),
                             rating=request.form.get("rating"))
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    # or just go to the add page
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """
    The edit rating page.
    """
    with app.app_context():
        # get book id and book record
        book_id = request.args.get("id", type=int)
        book = db.session.get(Books, book_id)
        if request.method == "POST":
            # change the rating
            book.rating = request.form.get('new_rating')
            db.session.commit()
            return redirect(url_for('home'))
        # or download edit rating page
        return render_template("rating.html", book=book)


@app.route('/delete', methods=["GET"])
def delete():
    """
    The function for deleting record
    """
    with app.app_context():
        # get book id and delete record with it
        book_id = request.args.get("id", type=int)
        book = db.session.get(Books, book_id)
        db.session.delete(book)
        db.session.commit()
        # download home page after that
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

