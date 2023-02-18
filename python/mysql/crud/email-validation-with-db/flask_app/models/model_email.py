from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    DB = "email_schema"

    def __init__(self, data):
        self.email = data["email"]
    
    @staticmethod
    def validate(user):
        isValid = True
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address!")
            isValid = False
        if Email.read_one(user):
            flash("Email already exists!")
            isValid = False
        return isValid
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM emails;"
        return connectToMySQL(cls.DB).query_db(query)
    
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_one(cls, data):
        print(data)
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)