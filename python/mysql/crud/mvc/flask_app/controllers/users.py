from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route("/")
def index():
    return render_template("create.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.create(data)
    return redirect("/read_users")


@app.route("/read_users")
def read_users():
    users = User.read()
    return render_template("read.html", users=users)
