from flask import Flask, render_template, redirect, session, request
import random, secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()

def initialize():
    if("correct_number" not in session):
        session["correct_number"] = random.randint(1, 100)
    if("guess_number" not in session):
        session["guess_number"] = None

@app.route("/")
def index():
    initialize()
    print(session["guess_number"])
    return render_template("game.html", correct_number=session["correct_number"], guess_number=session["guess_number"])

@app.route("/guess", methods=["POST"])
def guess():
    session["guess_number"] = int(request.form["guess_number"])
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)