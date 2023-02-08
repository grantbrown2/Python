from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.full_name = data['first_name'] + " " + data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at ) VALUES (%(firstName)s, %(lastName)s , %(email)s , NOW(), NOW() )"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def remove_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def edit_user_info(cls, data):
        query = "UPDATE users SET first_name = %(firstName)s,last_name = %(lastName)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)


    # VALIDATION METHOD
    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['firstName']) < 1:
            flash("First Name must be at least 2 characters long!")
            is_valid = False
        if len(user['lastName']) < 1:
            flash("Last Name must be at least 2 characters long!")
            is_valid = False
        if len(user['email']) < 1:
            flash("Email must be at least 2 characters long!")
            is_valid = False
        return is_valid

    
    @staticmethod
    def email_validate(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format!")
            is_valid = False
        return is_valid