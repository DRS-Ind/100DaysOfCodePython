from datetime import datetime
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, InputRequired

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
# generate csrf token
app.secret_key = "asdf2efa4ga"
bootstrap = Bootstrap5(app)


class LoginForm(FlaskForm):
    """
    The login form.
    """
    email = StringField(label="email", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label="password",
                             validators=[InputRequired(), Length(min=8, message="At least 8 character")])
    submit = SubmitField(label="Log In")


@app.context_processor
def context_now():
    """
    The function adds possibility to call datetime.datetime.now()
    :return: you call now in html jinja
    """
    return {"now": datetime.now()}


@app.route("/")
def home():
    """
    The home page.
    """
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    The login page.
    """
    # initialize login form
    form = LoginForm()

    # if form submitting (method POST)
    if form.validate_on_submit():
        # check good credentials
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        # else render bad access page
        return render_template("denied.html")

    # if method GET render login page
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
