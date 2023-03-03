from flask_app import bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models.model_user import User

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Category:
    DB = "budget_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
    
    @classmethod
    def create(cls, data):
        if cls.read_one(data):
            flash("That category already exists!", "text-danger")
            return False
        query = "INSERT INTO categories (user_id, name) VALUES (%(user_id)s, %(name)s);"
        flash("Successfully added category.", "text-success")
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM categories WHERE user_id = %(user_id)s AND name = %(name)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def read_all_by_user_id(cls, data):
        query = "SELECT * FROM categories WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return []
        all_categories = []
        for result in results:
            all_categories.append(cls(result))
        return all_categories
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM categories WHERE id = %(id)s AND user_id = %(user_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)