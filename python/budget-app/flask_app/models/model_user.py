from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "budget_schema"

    def __init__(self, data):
        self.user = data["user"]
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (user) VALUES (%(user)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(cls.DB).query_db(query)
    
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM users WHERE user = %(user)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_one(cls, data):
        print(data)
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @staticmethod
    def validate_login(user):
        isValid = True
        print(user)
        if not EMAIL_REGEX.match(user["user"]):
            flash("Invalid user address!")
            isValid = False
        if User.read_one(user):
            flash("User already exists!")
            isValid = False
        return isValid
    
    @staticmethod
    def validate_register(user):
        isValid = True
        if not EMAIL_REGEX.match(user["user"]):
            flash("Invalid user address!")
            isValid = False
        if User.read_one(user):
            flash("User already exists!")
            isValid = False
        return isValid