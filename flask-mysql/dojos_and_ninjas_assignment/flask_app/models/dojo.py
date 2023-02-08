from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data ['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(dojoName)s, NOW(), NOW())"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    # Joining the ninjas to dojos/ONE TO MANY
    @classmethod
    def join(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo



    # VALIDATION EXAMPLE
    @staticmethod
    def validation_dojo(dojo):
        is_valid = True
        if len(dojo['dojoName']) < 2:
            flash("Name must be at least 2 characters")
            is_valid = False 
        return is_valid




    # EMAIL VALIDATION EXAMPLE
    import re
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    @staticmethod
    def email_validate(dojo):
        is_valid = True
        if not EMAIL_REGEX.match(dojo['email']):
            flash("Invalid email address!", 'email')
            is_valid = False
        return is_valid

    # Say we want to categorize flash messages into different labels or buckets. 
    # We can utilize categories by passing a second argument in the flash function:
    # flash ("Email cannot be blank!", 'email')