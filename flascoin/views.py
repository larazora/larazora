from flask import render_template, url_for
from flascoin import app

@app.route("/")
def greeting():
    return render_template("index.html", message = "Hello world!")
