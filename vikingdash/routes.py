from vikingdash import app, coopertitions
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
        current=coopertitions.find({"completed": False}),
        past=coopertitions.find({"completed": True})
    )

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    alert = None
    if request.method == "POST":
        form = request.form
        mycoop = Coopertition(form["red"].split(","), form["blue"].split(","), form["name"], american_time(form["time"]), form["redname"], form["bluename"])
        if coopertitions.find_one({"name": form["name"]}):
            alert = "Name already taken!"
        else:
            coopertitions.insert_one(mycoop.export())
            alert = f"Successfully added coopertition {form['name']}!"
            reset_kiosk()

    coops = list(coopertitions.find({"completed": False}))
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
    query = coopertitions.update_one({"name": request.json["match"]}, {"$set": {"completed": True, "redpoints": request.json["red"], "bluepoints": request.json["blue"]}})
    reset_kiosk()
    return "OK"

@app.route("/setstatus", methods=["POST"])
def setstatus():
    status.set_status(request.json["status"])
    reset_kiosk()
    return "OK"

@app.route("/delete", methods=["POST"])
def delete():
    query = coopertitions.delete_one({"name": request.json["match"]})
    reset_kiosk()
    print(query.deleted_count)
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
    coopertitions.delete_many({})
    reset_kiosk()
    return "OK"