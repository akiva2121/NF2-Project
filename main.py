from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import os
import smtplib



app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/treatment")
def treatment():
    return render_template("treatment.html")

@app.route("/symptoms")
def symptoms():
    return render_template("symptoms.html")

@app.route("/diagnosis")
def diagnosis():
    return render_template("diagnosis.html")



MAIL_ADDRESS = os.environ.get("EMAIL_KEY")
MAIL_APP_PW = os.environ.get("PASSWORD_KEY")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MAIL_ADDRESS, MAIL_APP_PW)
        connection.sendmail(MAIL_ADDRESS, email, email_message)




if __name__ == "__main__":
    app.run(debug=True, port=5007)