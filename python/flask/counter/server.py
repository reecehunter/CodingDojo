from flask import Flask, render_template, redirect, session, request
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()

# # #
# Helper functions
# # #

def initialize_session(key, value):
    if str(key) not in session:
        session[str(key)] = value

def edit_session(key, value):
    initialize_session(key, value)
    session[str(key)] = value

# # #
# Routing
# # #

@app.route("/")
def index():
    initialize_session("count", 0)
    initialize_session("visits", 0)
    edit_session("count", session["count"] + 1)
    edit_session("visits", session["visits"] + 1)
    return render_template("counter.html", count=session["count"], visits=session["visits"])

@app.route("/amount", methods=["POST"])
def amount():
    amount = request.form["increment-amount"]
    return redirect(f"/amount/{str(amount)}")

@app.route("/amount/<int:amount>")
def count_two(amount):
    if session.get("count") == None:
        return redirect("/")
    edit_session("count", session["count"] + amount)
    edit_session("visits", session["visits"] + 1)
    return render_template("counter.html", count=session["count"], amount=amount, visits=session["visits"])

@app.route("/destroy_session/<string:key>")
def destroy_session(key):
    session.pop(key)
    return redirect("/")

# # #
# Start app
# # #

if __name__ == "__main__":
    app.run(debug=True)