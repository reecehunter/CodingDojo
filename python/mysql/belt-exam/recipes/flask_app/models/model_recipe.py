from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

class Recipe:
    DB = "recipes"

    def __init__(self, data):
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instructions) VALUES (%(name)s, %(description)s, %(instructions)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM recipes;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = id;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate(data):
        isValid = True
        if len(data["name"]) < 3:
            flash("Name must be more than 3 characters.")
            isValid = False
        if len(data["description"]) < 3:
            flash("Description must be more than 3 characters.")
            isValid = False
        if len(data["instructions"]) < 3:
            flash("Instructions must be more than 3 characters.")
            isValid = False
        return isValid

    @staticmethod
    def validate_create(data):
        isValid = True
        if User.read_one(data):
            flash("Email already exists!")
            isValid = False
        if len(data["fname"]) < 2:
            flash("Your first name must be greater than 2 characters.")
            isValid = False
        if len(data["lname"]) < 2:
            flash("Your last name must be greater than 2 characters.")
            isValid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!")
            isValid = False
        if len(data["password"]) < 8:
            flash("Your password must be at least 8 characters.")
            isValid = False
        return isValid