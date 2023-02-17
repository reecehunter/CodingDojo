from flask_app import app
from flask import redirect
from flask_app.controllers import controller_dojo

@app.route("/")
def index():
    return redirect("/dojos")


if __name__ == "__main__":
    app.run(debug=True)
