import os
import requests
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, SubmitField, FloatField
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask import Flask, render_template, redirect, url_for, request

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# load environment variables
load_dotenv()


# Prepare model class for SQLAlchemy
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# initialize database, bootstrap and configuration for flask
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-database.db"
Bootstrap5(app)
db.init_app(app)

# GLOBAL VARIABLES
HEADER = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ["BEAVER"]}"
}


class Movie(db.Model):
    """
    The database table.
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[float] = mapped_column(Float)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250))


class UpdateRating(FlaskForm):
    """
    The Flask WTForms for updating rating.
    """
    rating = FloatField('Your rating out of 10',
                        validators=[DataRequired(), NumberRange(min=0, max=10, message="Try number between 0 and 10")])
    review = StringField('Your review', validators=[DataRequired()])
    submit_button = SubmitField('Done')


class AddMovie(FlaskForm):
    """
    The Flask WTForms for adding movie.
    """
    title = StringField("Movie Title", validators=[DataRequired()])
    add_button = SubmitField("Add Movie")


def find_movie(movie_name: str) -> list:
    """
    The function finds movie from TMDB database.
    :param movie_name: the movie title
    :return: list with movies
    """
    params = {
        "query": movie_name
    }
    url = "https://api.themoviedb.org/3/search/movie"
    response = requests.get(url, headers=HEADER, params=params).json()["results"]
    return response


def get_movie_detail(tmdb: int) -> Movie:
    """
    The function gets detail about movie.
    :param tmdb: tmdb id
    :return: prepared Movie class
    """
    url = f"https://api.themoviedb.org/3/movie/{tmdb}"
    response = requests.get(url, headers=HEADER).json()
    new_movie = Movie(
        title=response["title"],
        year=response["release_date"][:4],
        description=response["overview"],
        rating=None,
        ranking=response["vote_average"],
        review=None,
        img_url=f"https://image.tmdb.org/t/p/w500{response["poster_path"]}"
    )
    return new_movie


# CREATE TABLE
# with app.app_context():
#     db.create_all()
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    """
    The home page.
    """
    db_data = Movie.query.order_by(Movie.rating.desc()).all()
    return render_template("index.html", movies=db_data)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    """
    The edit page. The URL contain 'id' parameter.
    """
    with app.app_context():
        movie_id = request.args.get("id")
        movie_to_update = Movie.query.get(movie_id)
        form = UpdateRating()
        if form.validate_on_submit():
            # update and save changes, then go to the home page
            movie_to_update.rating = request.form.get("rating")
            movie_to_update.review = request.form.get("review")
            db.session.commit()
            return redirect(url_for('home'))
        return render_template("edit.html", form=form, movie=movie_to_update)


@app.route("/delete")
def delete():
    """
    The endpoint deletes movie from database. The URL contain 'id' parameter.
    """
    with app.app_context():
        movie_id = request.args.get("id")
        movie_to_delete = Movie.query.get_or_404(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def select():
    """
    The find page.
    """
    with app.app_context():
        form = AddMovie()
        if form.validate_on_submit():
            # get title from form and go to the page with movie list
            movie_title = request.form.get("title")
            movies = find_movie(movie_name=movie_title)
            return render_template("select.html", result=movies)
        return render_template("add.html", form=form)


@app.route("/add-movie")
def add():
    """
    The endpoint adds movie to the database. The URL contain 'id' parameter.
    """
    with app.app_context():
        tmdb_id = request.args.get("id", type=int)
        new_movie = get_movie_detail(tmdb=tmdb_id)
        db.session.add(new_movie)
        db.session.commit()
        # go to the edit page after adding the movie
        return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
