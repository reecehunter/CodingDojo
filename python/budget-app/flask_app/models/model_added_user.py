from flask_app import bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models.model_user import User

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class AddedUser:
    DB = "budget_schema"

    def __init__(self, data):
        self.user_id = data["user_id"]
        self.added_user_id = data["added_user_id"]
    
    @classmethod
    def create(cls, data):
        if cls.read_one({"user_id":data["user_id"], "added_user_id":data["added_user_id"]}):
            flash("That user is already added!", "text-danger")
            return False
        query = "INSERT INTO added_users (user_id, added_user_id) VALUES (%(user_id)s, %(added_user_id)s);"
        flash("Successfully added user.", "text-success")
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM added_users WHERE user_id = %(user_id)s AND added_user_id = %(added_user_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def read_all_by_user_id(cls, data):
        query = "SELECT * FROM added_users JOIN users ON added_users.added_user_id = users.id WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        added_users = []
        for result in results:
            added_users.append({
                "user": User.read_one_by_id({"id":result["added_user_id"]}),
                "added_user": cls(result)
            })
        return added_users
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM added_users WHERE user_id = %(user_id)s AND added_user_id = %(added_user_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)