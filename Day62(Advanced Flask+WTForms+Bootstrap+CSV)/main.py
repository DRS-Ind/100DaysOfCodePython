from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    # check url box for valid url address
    url = StringField('Cafe Location on Google Maps (URL)', validators=[URL(message="Invalid URL")])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 8:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Cofee Rating',
                                choices=("✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"),
                                validators=[DataRequired()])
    wifi_rating = SelectField('WiFi Sterenght Rating',
                              choices=("✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"),
                              validators=[DataRequired()])
    power_rating = SelectField('Power Socket Rating',
                               choices=("✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"),
                               validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    """
    The home page.
    """
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    """
    The page with form for adding new cafe revision.
    """
    form = CafeForm()
    # checks if form submitted
    if form.validate_on_submit():
        # if True, save answer and redirect to the all cafes page
        with open(file="cafe-data.csv", mode="a", encoding="UTF-8") as csv_file:
            csv_file.write("\n"+",".join([
                form.cafe.data,
                form.url.data,
                form.opening_time.data,
                form.closing_time.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_rating.data]))
            return redirect(url_for('cafes'))
    # if False, render the form page
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    """
    The page with all cafe revisions.
    """
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
