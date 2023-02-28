from flask_app import app
from flask import redirect, session, request, flash
from flask_app.models.model_user import User
from flask_app.models.model_added_user import AddedUser

@app.route("/added_users/add", methods=["POST"])
def add_added_user():
    if "user" not in session:
        return redirect("/login")
    added_user_id = User.read_one({"email":request.form["email"]})
    if not added_user_id:
        flash("There is no user associated with that email!", 'text-danger')
        return redirect("/profile")
    data = {
        "user_id": request.form["id"],
        "added_user_id": added_user_id.id
    }
    AddedUser.create(data)
    return redirect("/profile")

@app.route("/added_users/delete/<int:user_id>/<int:added_user_id>")
def delete_added_user(user_id, added_user_id):
    if "user" not in session:
        return redirect("/login")
    data = {
        "user_id": user_id,
        "added_user_id": added_user_id
    }
    AddedUser.delete_one(data)
    return redirect("/profile")