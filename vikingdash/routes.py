from vikingdash import app, db
from vikingdash.models import Status, Reloader, Coopertition
from vikingdash.methods import american_time
from flask import render_template, request, redirect, url_for

status = Status("Welcome other teams!")
reloader  = Reloader()

@app.route("/")
def index():
    return render_template(
        "index.html",
        status=status,
        current=Coopertition.query.filter_by(completed = False).all(),
        past=Coopertition.query.filter_by(completed = True).all()
    )

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    alert = None
    if request.method == "POST":
        form = request.form
        mycoop = Coopertition(
            red = form["red"],
            blue = form["blue"],
            name = form["name"],
            time = american_time(form["time"]),
            redname = form["redname"],
            bluename = form["bluename"],
            completed = False
        )
        if Coopertition.query.filter_by(name = form["name"]).first():
            alert = "Name already taken!"
        else:
            db.session.add(mycoop)
            db.session.commit()
            alert = f"Successfully added coopertition {form['name']}!"
            reset_kiosk()

    coops = Coopertition.query.filter_by(completed = False).all()
    return render_template(
        "backend.html",
        status=status,
        alert=alert,
        coopertitions=coops
    )

@app.route("/redirect")
def redirect_dash():
    return redirect(url_for("dashboard"))

@app.route("/archive", methods=["POST"])
def archive():
    query = Coopertition.query.filter_by(name = request.json["match"]).first()
    query.completed = True
    query.redpoints = request.json["red"]
    query.bluepoints = request.json["blue"]
    db.session.commit()
    reset_kiosk()
    return "OK"

@app.route("/setstatus", methods=["POST"])
def setstatus():
    status.set_status(request.json["status"])
    reset_kiosk()
    return "OK"

@app.route("/delete", methods=["POST"])
def delete():
    query = Coopertition.query.filter_by(name = request.json["match"]).first()
    db.session.delete(query)
    db.session.commit()
    reset_kiosk()
    return "OK"

@app.route("/reload", methods=["GET"])
def reload_prompt() -> dict:
    if reloader.reload:
        reloader.reload = False
        return {"reload": True}
    else:
        return {"reload": False}
    
@app.route("/reset_kiosk", methods=["GET"])
def reset_kiosk():
    reloader.reload = True
    return "OK"

@app.route("/delete_all", methods=["GET"])
def delete_all_coopertitions():
    queries = Coopertition.query.all()
    for i in queries:
        db.session.delete(i)
    db.session.commit()
    reset_kiosk()
    return "OK"