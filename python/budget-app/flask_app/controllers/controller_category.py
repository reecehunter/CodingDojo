from flask_app import app
from flask import redirect, session, request, flash
from flask_app.models.model_user import User
from flask_app.models.model_category import Category

@app.route("/category/add", methods=["POST"])
def add_category():
    if "user" not in session:
        return redirect("/login")
    Category.create(request.form)
    year = request.form["year"]
    month = request.form["month"]
    return redirect(f"/budget/{year}/{month}")

@app.route("/category/delete", methods=["POST"])
def delete_category():
    if "user" not in session:
        return redirect("/login")
    Category.delete(request.form)
    year = request.form["year"]
    month = request.form["month"]
    return redirect(f"/budget/{year}/{month}")