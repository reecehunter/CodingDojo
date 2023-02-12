from flask import Flask, render_template, session, redirect, request
import secrets, random

app = Flask(__name__)
app.secret_key = secrets.token_hex()

def start_game():
    if("gold" not in session):
        session["gold"] = 0
    if("activities" not in session):
        session["activities"] = ["You entered the world."]

@app.route("/")
def index():
    start_game()
    return render_template("index.html", gold=session["gold"], activities=session["activities"])

@app.route("/process_money", methods=["POST"])
def process_money():
    if(str("gold") not in session):
        return redirect("/")

    building = request.form["building"]
    amount = 0

    if(building == "farm"):
        amount = random.randint(10, 20)
    elif(building == "cave"):
        amount = random.randint(5, 10)
    elif(building == "house"):
        amount = random.randint(2, 5)
    elif(building == "casino"):
        amount = random.randint(-50, 50)

    earned = "Earned"
    if amount < 0:
        earned = "Lost"

    session["activities"].append(f"{earned} {amount} at the {building}.")
    session["gold"] += amount

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)