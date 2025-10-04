from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql.expression import func

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    """
    The SQL table.
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


def serialize_cafe_class(cafe=Cafe) -> dict:
    """
    The function serialize SQL table row into the dictionary.

    :param cafe: The SQL table Cafe
    :return: The SQL table row in dict format
    """
    return {
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price,
        "has_socket": cafe.has_sockets,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "id": cafe.id,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "map_url": cafe.map_url,
        "name": cafe.name,
        "seats": cafe.seats
    }


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    """
    The home page.
    """
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    """
    The API response with information about random cafe.
    :return: cafe`s information in json format
    """
    random_cafe = Cafe.query.order_by(func.random()).first()
    return jsonify(cafe=serialize_cafe_class(cafe=random_cafe))


@app.route("/all")
def get_all_cafes():
    """
    The API endpoint gets an information about all cafes in the database.
    :return: cafes` information in json format
    """
    all_cafes = [serialize_cafe_class(cafe=cafe) for cafe in Cafe.query.all()]
    return jsonify(cafe=all_cafes)


@app.route("/search")
def search_cafe():
    """
    The API response with information about certain cafe.
    :return: cafes` information in json format
    """
    location = request.args.get("loc")
    searched_cafe = Cafe.query.filter(Cafe.location == location).all()
    all_cafes = [serialize_cafe_class(cafe=cafe) for cafe in searched_cafe]
    return jsonify(cafe=all_cafes)


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    """
    The API endpoint adds new cafe to the database.
    :return: response about success in json format
    """
    with app.app_context():
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=request.form.get("has_toilet") == "true",
            has_wifi=request.form.get("has_wifi") == "true",
            has_sockets=request.form.get("has_sockets") == "true",
            can_take_calls=request.form.get("can_take_calls") == "true",
            coffee_price=request.form.get("coffee_price")
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={
            "success": "Successfully added the new cafe."
        })


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id: int):
    """
    The API endpoint update coffee price of the certain cafe.
    :param cafe_id: cafe id
    :return: response with result in json format
    """
    new_price = request.args.get("new_price")
    cafe = db.session.get(entity=Cafe, ident=cafe_id)  # Returns None if cafe_id is not found
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    # rise 404 HTML error if cafe id is not found
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id: int):
    """
    The API endpoint delete database`s record of the certain cafe.
    :param cafe_id: cafe id
    :return: response with result in json format
    """
    if request.args.get("api-key") == "TopSecretAPIKey":
        cafe = db.session.get(entity=Cafe, ident=cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200
        # rise 404 HTML error if cafe id is not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    # rise 403 HTML error if api key valid
    return jsonify(response={"error": "Sorry, that`s not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
