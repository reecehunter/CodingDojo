from flask_app import app, bcrypt
from flask import redirect, request, session, render_template
from flask_app.models.model_user import User
from flask_app.models.model_added_user import AddedUser

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
    User.create(data)
    session["user"] = request.form
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
    # Get all user-owned budget sheets and pass them into the template
    return render_template("dashboard.html")

@app.route("/dashboard/shared")
def dashboard_shared():
    if "user" not in session:
        return redirect("/login")
    # Get all shared budget sheets and pass them into the template
    return render_template("dashboard.html")

@app.route("/budget")
def budget():
    if "user" not in session:
        return redirect("/login")
    return render_template("budget.html")