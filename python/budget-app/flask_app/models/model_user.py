from flask_app import bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "budget_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (username, first_name, last_name, email, password) VALUES (%(username)s, %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(cls.DB).query_db(query)
    
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def read_one_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET username=%(username)s, first_name=%(first_name)s, last_name=%(last_name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def login(cls, data):
        user_in_db = cls.read_one(data)
        if not bcrypt.check_password_hash(user_in_db.password, data["password"]):
            flash("Invalid login credentials.", 'text-danger')
            return False
        return user_in_db
    
    @staticmethod
    def validate_update(user):
        isValid = True
        if len(user["username"]) < 3:
            flash("Username must be at least 3 characters!", 'text-danger')
            isValid = False
        if len(user["first_name"]) < 2:
            flash("First name must be at least 2 characters!", 'text-danger')
            isValid = False
        if len(user["last_name"]) < 2:
            flash("Last name must be at least 2 characters!", 'text-danger')
            isValid = False
        return isValid
    
    @staticmethod
    def validate_login(user):
        isValid = True
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email format!", 'text-danger')
            isValid = False
        if len(user["password"]) < 8:
            flash("Passwords are at least 8 characters!", 'text-danger')
            isValid = False
        if not User.read_one(user):
            flash("Invalid login credentials.", 'text-danger')
            isValid = False
        return isValid
    
    @staticmethod
    def validate_register(user):
        isValid = True
        if len(user["username"]) <= 2:
            flash("Username must be at least 3 characters!", 'text-danger')
            isValid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid user address!", 'text-danger')
            isValid = False
        if len(user["first_name"]) < 2:
            flash("First name must be at least 2 characters!", 'text-danger')
            isValid = False
        if len(user["last_name"]) < 2:
            flash("Last name must be at least 2 characters!", 'text-danger')
            isValid = False
        if len(user["password"]) < 8:
            flash("Passwords must be at least 8 characters!", 'text-danger')
            isValid = False
        if user["password"] != user["confirm_password"]:
            flash("Passwords must match!", 'text-danger')
            isValid = False
        if User.read_one(user):
            flash("User already exists!", 'text-danger')
            isValid = False
        return isValid