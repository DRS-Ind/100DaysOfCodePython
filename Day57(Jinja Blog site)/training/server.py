import datetime
from flask import Flask, render_template
import random
import requests


app = Flask(__name__, template_folder="./templates")
current_year = datetime.datetime.now().year


@app.route("/")
def home():
    rand_num = random.randint(1, 10)
    return render_template("index.html", rand_num=rand_num, current_year=current_year)


@app.route("/guess/<name>")
def guess_age_and_sex(name: str):
    age_url = "https://api.agify.io"
    sex_url = "https://api.genderize.io"
    params = {"name": name}
    your_age_prob = requests.get(url=age_url, params=params).json()["age"]
    your_sex_prob = requests.get(url=sex_url, params=params).json()["gender"]
    return render_template("guess.html", name=name.title(), age=your_age_prob, sex=your_sex_prob, current_year=current_year)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(url=blog_url).json()
    return render_template("blog.html", blogs_data = all_posts, current_year=current_year)


if __name__ == '__main__':
    app.run(debug=True)