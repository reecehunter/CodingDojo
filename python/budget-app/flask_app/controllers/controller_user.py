from flask_app import app, bcrypt
from flask import redirect, request, session, render_template, flash
from flask_app.models.model_user import User
from flask_app.models.model_added_user import AddedUser
from flask_app.models.model_category import Category
from flask_app.models.model_entry import Entry

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register/submit", methods=["POST"])
def register_submit():
    if not User.validate_register(request.form):
        return redirect("/register")
    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    created_user_id = User.create(data)
    if not created_user_id:
        flash("Error creating user.", "text-danger")
        return redirect("/register")
    session["user"] = User.read_one_by_id({"id":created_user_id}).__dict__
    return redirect("/dashboard")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login/submit", methods=["POST"])
def login_submit():
    if not User.validate_login(request.form):
        return redirect("/login")
    user_in_db = User.login(request.form)
    if not user_in_db:
        return redirect("/login")
    session["user"] = user_in_db.__dict__
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    if "user" not in session:
        return redirect("/login")
    session.pop("user")
    return redirect("/login")

@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")
    user = User.read_one({"email":session["user"]["email"]})
    added_users = AddedUser.read_all_by_user_id({"user_id":user.id})
    print(added_users)
    return render_template("profile.html", user=user, added_users=added_users)

@app.route("/profile/update", methods=["POST"])
def update_profile():
    if "user" not in session:
        return redirect("/login")
    if not User.validate_update(request.form):
        return redirect("/profile")
    User.update(request.form)
    return redirect("/profile")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    user_id = session["user"]["id"]
    entries = Entry.read_dates_by_user_id({"user_id":user_id})
    # month_values = {
    #     1: "January",
    #     2: "February",
    #     3: "March",
    #     4: "April",
    #     5: "May",
    #     6: "June",
    #     7: "July",
    #     8: "January",
    #     9: "January",
    #     10: "January",
    #     11: "January",
    #     12: "January",
    # }
    if not entries:
        flash("There was an error getting your budget sheets.", "text-danger")
        redirect("/dashboard")
    return render_template("dashboard.html", entries=entries)

@app.route("/dashboard/shared")
def dashboard_shared():
    if "user" not in session:
        return redirect("/login")
    # Get all shared budget sheets and pass them into the template
    return render_template("dashboard.html")

@app.route("/budget/<int:year>/<int:month>")
def budget(year, month):
    if "user" not in session:
        return redirect("/login")
    user_id = session["user"]["id"]
    data = {
        "user_id": user_id,
        "year": year,
        "month": month
    }
    entries = Entry.read_all_by_user_id_and_date(data)
    categories = Category.read_all_by_user_id(data)
    if not entries:
        flash("Entries not found.", "text-danger")
        return redirect(f"/budget/{year}/{month}")
    if not categories:
        flash("Categories not found.", "text-danger")
        return redirect(f"/budget/{year}/{month}")
    print(entries)
    return render_template("budget.html", user=session["user"], entries=entries, categories=categories, year=year, month=month)