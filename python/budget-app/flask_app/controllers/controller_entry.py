from flask_app import app
from flask import redirect, session, request, flash
from flask_app.models.model_entry import Entry

@app.route("/entry/add", methods=["POST"])
def add_entry():
    if "user" not in session:
        return redirect("/login")
    year = request.form["year"]
    month = request.form["month"]
    data = {
        **request.form,
        "date": f"{year}-{month}-01"
    }
    Entry.create(data)
    url = session["url"]
    return redirect(url)

@app.route("/entry/delete", methods=["POST"])
def delete_entry():
    if "user" not in session:
        return redirect("/login")
    Entry.delete(request.form)
    return redirect("/budget")