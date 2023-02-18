from flask import flash

class Dojo:
    @staticmethod
    def validate(dojo):
        is_valid = True
        if len(dojo["name"]) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if dojo["location"] == None:
            flash("You must select a dojo location.")
            is_valid = False
        if dojo["language"] == None:
            flash("You must select a favorite language.")
            is_valid = False
        if len(dojo["comments"]) < 1:
            flash("You must leave a comment!")
            is_valid = False
        return is_valid