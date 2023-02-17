from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_ninja import Ninja
from datetime import datetime


@app.route("/ninja/create")
def ninja_create():
    return render_template("create_ninja.html")

@app.route("/ninja/create/submit", methods=["POST"])
def ninja_create_submit():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    Ninja.create(data)
    return redirect("/ninjas")


@app.route("/ninja/edit/<int:id>")
def ninja_edit(id):
    data = {
        "id": id
    }
    session["ninja"] = Ninja.read_one(data)
    return render_template("edit_ninja.html", ninja=session["ninja"])

@app.route("/ninja/edit/submit", methods=["POST"])
def ninja_edit_submit():
    id = request.form["id"]
    data = {
        "id": id,
        "dojoid": request.form["dojoid"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "time": datetime.now(),
    }
    Ninja.update_one(data)
    return redirect(f"/ninja/get/{id}")


@app.route("/ninja/delete/<int:id>")
def ninja_delete(id):
    data = {
        "id": id
    }
    Ninja.delete(data)
    return redirect("/ninjas")


@app.route("/ninja/get/<int:id>")
def ninja_get(id):
    data = {
        "id": id
    }
    session["ninja"] = Ninja.read_one(data)
    return render_template("read_ninja.html", ninja=session["ninja"])


@app.route("/ninjas")
def ninjas_show():
    ninjas = Ninja.read_all()
    return render_template("read_ninjas.html", ninjas=ninjas)