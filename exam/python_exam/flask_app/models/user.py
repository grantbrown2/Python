from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile('[A-Z]')
db = "exam_schema"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.full_name = data['first_name'] + " " + data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def registration_validation(user):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(db).query_db(query,user)
        is_valid = True
        if len(user['first_name']) < 2:
            flash(u"First name must be at least 2 characters.", "registration_error")
            is_valid = False
        if len(user['last_name']) < 2:
            flash(u"Last name must be at least 2 characters.", "registration_error")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", 'email')
            is_valid = False
        if len(results) >= 1:
            flash(u"Email is already taken!", "registration_error")
            is_valid = False
        if not PASSWORD_REGEX.search(user['password']):
            flash(u"Password must have at least 1 uppercase letter!", "registration_error")
            is_valid = False
        if len(user['password']) < 8:
            flash(u"Password must have at least 8 characters.", "registration_error")
            is_valid = False
        if not user['confirm_password'] == user['password']:
            flash(u"Passwords do not match!", "registration_error")
            is_valid = False
        return is_valid