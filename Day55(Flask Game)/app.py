from flask import Flask
from random import randrange
from functools import wraps


random_number = randrange(start=1, stop=10)
app = Flask(__name__)


def make_header(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<h1>{result}</h1>"
    return wrapper


@app.route("/")
@make_header
def hello_page():
    return "Add your number to URL and guess the number between 1 and 10"


@app.route("/<int:number>")
def guess_number(number: int):
    if number == random_number:
        return "You`re guessed"
    elif number > random_number:
        return "Too big"
    else:
        return "Too low"


if __name__ == '__main__':
    app.run(debug=True)
