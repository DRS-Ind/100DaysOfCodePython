from flask import Flask, render_template
from post import Post


app = Flask(__name__)
post = Post()

@app.route('/blog')
def home():
    return render_template("index.html", blog_data=post.get_all_posts())


@app.route("/post/<int:post_id>")
def get_post(post_id):
    return render_template("post.html", post=post.get_post(post_id=post_id))


if __name__ == "__main__":
    app.run(debug=True)
