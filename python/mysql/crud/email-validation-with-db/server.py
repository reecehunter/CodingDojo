from flask_app import app
from flask import render_template
from flask_app.controllers import controller_email

@app.route("/")
def index():
    return render_template("create_email.html")

if __name__ == "__main__":
    app.run(debug=True)