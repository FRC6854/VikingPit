from vikingdash import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
@app.route("/dash")
def dashboard():
    return render_template("backend.html")