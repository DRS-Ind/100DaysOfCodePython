import os
import ssl
import socket
import smtplib
import datetime
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()


app = Flask(__name__, template_folder="templates")
post_data = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7").json()
curr_year = datetime.datetime.now().year


@app.route("/")
def home():
    return render_template(template_name_or_list="index.html", posts=post_data, current_year=curr_year)


@app.route("/contact", methods=["GET"])
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
        return render_template(template_name_or_list="response.html", current_year=curr_year, title="Error 404",
                               subtitle="Your page is not found.")
    else:
        return render_template(template_name_or_list="post.html", post=post_info, current_year=curr_year)


@app.route("/contact", methods=["POST"])
def receive_form_data():
    form_name = request.form['name']
    form_email = request.form['email']
    form_phone = request.form['tel']
    form_message = request.form['message']
    company_email = os.environ["COMPANY_EMAIL"]
    company_email_password = os.environ["COMPANY_EMAIL_PASS"]
    completed_message = (f"Get response from {form_name}.\n"
                         f"Email: {form_email}. Phone: {form_phone}.\n"
                         f"Message: {form_message}")
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl.create_default_context()) as connection:
            connection.login(user=company_email, password=company_email_password)
            connection.sendmail(from_addr=company_email, to_addrs=company_email,
                                msg=f"Subject:Response from form\n\n{completed_message}")
    except (smtplib.SMTPException, socket.gaierror):
        return render_template(template_name_or_list="response.html", current_year=curr_year, title="Error 500",
                               subtitle="Your message has not been sent.")
    return render_template(template_name_or_list="response.html", current_year=curr_year, title="Hooray",
                           subtitle="Successfully sent your message.")


if __name__ == '__main__':
    app.run(debug=True)
