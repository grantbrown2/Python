from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user

db = "exam_schema"

class Sasquatch:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.date_seen = data['date_seen']
        self.count = data['count']
        self.user_id = data['user_id']
        self.posted_by = None

    @classmethod
    def add_sasquatch(cls, data):
        query = "INSERT INTO sasquatch (location, what_happened, date_seen, count, user_id) VALUES (%(location)s, %(what_happened)s, %(date_seen)s, %(count)s, %(user_id)s)"
        result = connectToMySQL(db).query_db(query,data)
        return result

    @classmethod
    def join(cls):
        query = "SELECT * FROM sasquatch JOIN users ON sasquatch.user_id = users.id"
        results = connectToMySQL(db).query_db(query)
        sasquatches = []
        for row_from_db in results:
            one_sasquatch = cls(row_from_db)
            sasquatch_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "email" : row_from_db["email"],
                "password" : "",
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            one_sasquatch.posted_by = user.User(sasquatch_data)
            sasquatches.append(one_sasquatch)
        return sasquatches

    @classmethod
    def get_sasquatch(cls, data):
        query = "SELECT * FROM sasquatch JOIN users ON sasquatch.user_id =  users.id WHERE sasquatch.id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        one_sasquatch = cls(results[0])
        for row_from_db in results:
            user_data = {
                    "id" : row_from_db["users.id"],
                    "first_name" : row_from_db["first_name"],
                    "last_name" : row_from_db["last_name"],
                    "email" : row_from_db["email"],
                    "password" : "",
                    "created_at" : row_from_db["created_at"],
                    "updated_at" : row_from_db["updated_at"]
                }
        one_sasquatch.posted_by = user.User(user_data)
        return one_sasquatch

    @classmethod
    def edit_sasquatch_in_db(cls, data):
        query = "UPDATE sasquatch SET location = %(location)s,what_happened = %(what_happened)s, date_seen = %(date_seen)s, count = %(count)s WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete_sasquatch_from_db(cls, data):
        query = "DELETE FROM sasquatch WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def sasquatch_validation(data):
        validation = True
        if len(data['location']) < 2:
            flash(u"Location must be at least 2 characters.", "sasquatch_error")
            validation = False
        if len(data['what_happened']) < 3:
            flash(u"Description must be at least 3 characters.", "sasquatch_error")
            validation = False
        if len(data['date_seen']) == 0:
            flash(u"You must choose a date spotted!", "sasquatch_error")
            validation = False
        if len(data['count']) < 1:
            flash(u"You must select at least 1 sasquatch!", "sasquatch_error")
            validation = False
        return validation