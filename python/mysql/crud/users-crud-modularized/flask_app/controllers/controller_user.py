from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_user import User
from datetime import datetime


@app.route("/user/create")
def user_crate():
    return render_template("create_user.html")

@app.route("/user/create/submit", methods=["POST"])
def user_create_submit():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.create(data)
    return redirect("/users")


@app.route("/user/edit/<int:id>")
def user_edit(id):
    data = {
        "id": id
    }
    session["user"] = User.read_one(data)
    return render_template("edit_user.html", user=session["user"])

@app.route("/user/edit/submit", methods=["POST"])
def user_edit_submit():
    id = request.form["id"]
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "time": datetime.now(),
    }
    User.update_one(data)
    return redirect(f"/user/get/{id}")


@app.route("/user/delete/<int:id>")
def user_delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/users")


@app.route("/user/get/<int:id>")
def user_get(id):
    data = {
        "id": id
    }
    session["user"] = User.read_one(data)
    return render_template("read_user.html", user=session["user"])


@app.route("/users")
def users_show():
    users = User.read_all()
    return render_template("read_users.html", users=users)