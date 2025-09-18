import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder="templates")
post_data = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7").json()
curr_year = datetime.datetime.now().year


@app.route("/")
def home():
    return render_template(template_name_or_list="index.html", posts=post_data, current_year=curr_year)


@app.route("/contact")
def contact():
    return render_template(template_name_or_list="contact.html", current_year=curr_year)


@app.route("/about")
def about():
    return render_template(template_name_or_list="about.html", current_year=curr_year)


@app.route("/post/<int:post_id>")
def post(post_id: int):
    try:
        post_info = post_data[post_id - 1]
    except IndexError:
        return render_template(template_name_or_list="404.html", current_year=curr_year)
    else:
        return render_template(template_name_or_list="post.html", post=post_info, current_year=curr_year)


if __name__ == '__main__':
    app.run(debug=True)
