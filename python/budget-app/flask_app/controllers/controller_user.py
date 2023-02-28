from flask_app import app
from flask import redirect, request, session, render_template
from flask_app.models.model_user import User

@app.route("/user/register")
def register():
    return render_template("register.html")

@app.route("/user/register/submit", methods=["POST"])
def register_submit():
    if not User.validate_register(request.form):
        return redirect("/")
    User.create(request.form)
    session["users"] = request.form
    return redirect("/dashboard")

@app.route("/user/login")
def login():
    return render_template("login.html")

@app.route("/user/login/submit")
def login_submit():
    if not User.validate_login(request.form):
        return redirect("/")
    session["users"] = request.form
    return redirect("/dashboard")

@app.route("/user/add/submit")
def add_user_submit():
    if "user" not in session:
        return redirect("/")
    return redirect("/dashboard")

@app.route("/user/profile")
def profile():
    # if "user" not in session:
    #     return redirect("/")
    return render_template("profile.html")
    
@app.route("/user/delete/<int:id>")
def delete_one(id):
    data = {
        "id": id
    }
    User.delete_one(data)
    return redirect("/")


@app.route("/dashboard")
def dashboard():
    # if "user" not in session:
    #     return redirect("/user/register")
    # Get all user-owned budget sheets and pass them into the template
    return render_template("dashboard.html")

@app.route("/dashboard/shared")
def dashboard_shared():
    # if "user" not in session:
    #     return redirect("/user/register")
    # Get all shared budget sheets and pass them into the template
    return render_template("dashboard.html")

# TEMPORARY! DELETE THIS!
@app.route("/budget")
def budget():
    return render_template("budget.html")