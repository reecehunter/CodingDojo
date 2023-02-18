from flask_app import app
from flask import redirect, request, session, render_template
from flask_app.models.model_email import Email

@app.route("/submit", methods=["POST"])
def submit():
    if not Email.validate(request.form):
        return redirect("/")
    Email.create(request.form)
    session["emails"] = request.form
    return redirect("/emails")
    
@app.route("/email/delete/<int:id>")
def delete_one(id):
    data = {
        "id": id
    }
    Email.delete_one(data)
    return redirect("/emails")

@app.route("/emails")
def emails():
    if "emails" not in session:
        return redirect("/")
    session["emails"] = Email.read_all()
    return render_template("read_emails.html", emails=session["emails"])