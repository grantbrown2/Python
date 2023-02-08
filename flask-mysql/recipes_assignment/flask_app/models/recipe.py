from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user

db = "recipes_schema"

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.posted_by = None

    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(user_id)s)"
        result = connectToMySQL(db).query_db(query,data)
        return result
    
    @classmethod
    def join(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id"
        results = connectToMySQL(db).query_db(query)
        recipes = []
        for row_from_db in results:
            one_recipe = cls(row_from_db)
            recipe_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "email" : row_from_db["email"],
                "password" : "",
                "created_at" : row_from_db["users.created_at"],
                "updated_at" : row_from_db["users.updated_at"]
            }
            one_recipe.posted_by = user.User(recipe_data)
            recipes.append(one_recipe)
        return recipes

    @classmethod
    def delete_recipe_from_db(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id =  users.id WHERE recipes.id = %(id)s"
        results = connectToMySQL(db).query_db(query, data)
        one_recipe = cls(results[0])
        print(results)
        print(one_recipe)
        for row_from_db in results:
            user_data = {
                    "id" : row_from_db["users.id"],
                    "first_name" : row_from_db["first_name"],
                    "last_name" : row_from_db["last_name"],
                    "email" : row_from_db["email"],
                    "password" : "",
                    "created_at" : row_from_db["users.created_at"],
                    "updated_at" : row_from_db["users.updated_at"]
                }
        one_recipe.posted_by = user.User(user_data)
        return one_recipe

    @classmethod
    def edit_recipe_in_db(cls, data):
        query = "UPDATE recipes SET name = %(name)s,description = %(description)s, instructions = %(instructions)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def recipe_validation(data):
        validation = True
        if len(data['name']) < 3:
            flash(u"Recipe name must be at least 3 characters.", "recipe_error")
            validation = False
        if len(data['description']) < 3:
            flash(u"Description must be at least 3 characters.", "recipe_error")
            validation = False
        if len(data['instructions']) < 3:
            flash(u"Instructions must be at least 3 characters.", "recipe_error")
            validation = False
        return validation