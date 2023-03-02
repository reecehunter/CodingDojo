from flask_app.config.mysqlconnection import connectToMySQL
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Entry:
    DB = "budget_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.category_id = data["category_id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.amount = data["amount"]
        self.date = data["date"]
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO entries (category_id, user_id, name, amount, date) VALUES (%(category_id)s, %(user_id)s, %(name)s, %(amount)s, %(date)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def read_all_by_user_id_and_date(cls, data):
        query = "SELECT *, categories.id AS category_category_id, categories.user_id AS category_user_id, categories.name AS category_name FROM entries JOIN categories ON entries.category_id = categories.id WHERE entries.user_id = %(user_id)s AND YEAR(date) = %(year)s AND MONTH(date) = %(month)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        all_entries = {}
        for result in results:
            if result["category_name"] not in all_entries:
                all_entries[result["category_name"]] = [cls(result)]
            else:
                all_entries[result["category_name"]].append(cls(result))
        return all_entries

    @classmethod
    def read_dates_by_user_id(cls, data):
        query = "SELECT date FROM entries WHERE entries.user_id = %(user_id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if not results:
            return False
        all_entries = {}
        for result in results:
            date = result["date"]
            year = str(date.year)
            if year not in all_entries:
                all_entries[year] = []
                for d in results:
                    if str(d["date"].year) == year and d["date"].month not in all_entries[year]:
                        all_entries[year].append(d["date"].month)
        return all_entries
    
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM entries WHERE id = %(id)s AND user_id = %(user_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)