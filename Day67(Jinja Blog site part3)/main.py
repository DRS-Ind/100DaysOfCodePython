from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class CreatePostForm(FlaskForm):
    post_title = StringField("Title", validators=[DataRequired()])
    post_subtitle = StringField("Subtitle", validators=[DataRequired()])
    post_author_name = StringField("Author`s name", validators=[DataRequired()])
    post_img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    post_body = CKEditorField("Post body", validators=[DataRequired()])
    post_submit = SubmitField("Add Post")


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/post')
def show_post():
    post_id = request.args.get("post_id")
    requested_post = BlogPost.query.where(BlogPost.id == post_id).first()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["POST", "GET"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post_data = BlogPost(
            title = request.form.get("post_title"),
            subtitle = request.form.get("post_subtitle"),
            date = date.today().strftime("%B %d,%Y"),
            body = request.form.get("post_body"),
            author = request.form.get("post_author_name"),
            img_url = request.form.get("post_img_url")
        )
        with app.app_context():
            db.session.add(new_post_data)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, is_new=True)


@app.route("/edit-post/<int:post_id>", methods=["POST", "GET"])
def edit_post(post_id: int):
    post = BlogPost.query.get_or_404(post_id)
    edit_form = CreatePostForm(
        post_title=post.title,
        post_subtitle=post.subtitle,
        post_img_url=post.img_url,
        post_author_name=post.author,
        post_body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.post_title.data
        post.subtitle = edit_form.post_subtitle.data
        post.img_url = edit_form.post_img_url.data
        post.author = edit_form.post_author_name.data
        post.body = edit_form.post_body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template("make-post.html", form=edit_form, is_new=False)


@app.route("/delete/<int:post_id>")
def delete_post(post_id: int):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
