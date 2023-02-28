from flask_app import app
from flask import redirect
from flask_app.controllers import controller_user

@app.route("/")
def index():
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)