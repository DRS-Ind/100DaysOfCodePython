from flask import Flask
from random import randrange


random_number = randrange(start=1, stop=10)
app = Flask(__name__)


def make_header_and_add_color(color_name):
    """
    The function adds <h1> tag to the all text and colors it.
    """
    def inner_function(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<h1 style="color: {color_name}">{result}</h1>'
        return wrapper
    return inner_function


def add_img(img_link):
    """
    The function adds image to the information in the page.

    :param img_link: link to the image
    """
    def inner_function(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{result}<img src="{img_link}" alt="context image">'
        return wrapper
    return inner_function


@app.route("/")
@add_img("https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif")
@make_header_and_add_color(color_name="black")
def hello_page():
    return "Guess a number between 0 and 9"

@add_img("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3psbmd6dmx1NWozOHplNG16M3hvcHlhc2lmZWRzZDR2dnhqYzU0diZlc"
         "D12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IuWMpDm2PdTL8s/giphy.gif")
@make_header_and_add_color(color_name="red")
def too_high_page():
    return 'Too high, try again'

@add_img("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXN1MGUydDV2eGl3MnhzaXBnZzlndDdpZXo0MDR1emVleGhoOGQ5YSZl"
         "cD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WfJyRpgey7o6HQi4Kk/giphy.gif")
@make_header_and_add_color(color_name="red")
def too_low_page():
    return 'Too low, try again'

@add_img("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnlrNno4aHg1bGZ2M25meHVrMWduYnF4czRqcXJhcTdjZnBzZHFtd"
         "yZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZYW3cN6hk2jHW/giphy.gif")
@make_header_and_add_color(color_name="green")
def you_found_page():
    return 'You found me'

@app.route("/<int:number>")
def guess_number(number: int):
    if number == random_number:
        return you_found_page()
    elif number > random_number:
        return too_high_page()
    else:
        return too_low_page()


if __name__ == '__main__':
    app.run(debug=True)
