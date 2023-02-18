from flask import Flask, render_template, request, redirect, session
import secrets
from models.model_dojo import Dojo

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.route("/")
def index():
    return render_template("survey.html")

@app.route("/submit", methods=["POST"])
def submit():
    if not Dojo.validate(request.form):
        return redirect("/")
    session["form-data"] = request.form
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html", data=session["form-data"])

if __name__ == "__main__":
    app.run(debug=True)