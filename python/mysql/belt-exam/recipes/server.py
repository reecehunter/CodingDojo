from flask_app import app
from flask import render_template
from flask_app.controllers.controller_user import User
from flask_app.controllers.controller_recipe import Recipe

@app.route("/")
def index():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)