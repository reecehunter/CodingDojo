from flask_app import app
from flask import redirect
from flask_app.controllers import controller_user
from flask_app.controllers import controller_added_user

@app.route("/")
def index():
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)