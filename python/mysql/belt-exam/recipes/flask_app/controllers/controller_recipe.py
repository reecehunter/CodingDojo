from flask_app import app
from flask import redirect, request, session, render_template, flash
from flask_bcrypt import Bcrypt
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe

bcrypt = Bcrypt(app)

@app.route("/recipe/create")
def recipe_create():
    if "user" not in session:
        return redirect("/")
    recipes = User.read_recipes()
    print(recipes)
    return render_template("create_recipe.html")

@app.route("/recipe/create/submit", methods=["POST"])
def recipe_create_submit():
    Recipe.create(request.form)
    return render_template("create_recipe.html")

@app.route("/recipes")
def success():
    if "user" not in session:
        return redirect("/")
    recipes = User.read_recipes()
    print(recipes)
    return render_template("recipes.html", data=session["user"], recipes=recipes)