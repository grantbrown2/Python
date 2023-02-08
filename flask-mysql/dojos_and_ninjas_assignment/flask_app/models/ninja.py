from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_ninjas(cls):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    # @classmethod
    # def get_ninja(cls, data):
    #     query = "SELECT * FROM ninjas WHERE id = %(id)s;"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    #     return cls(results[0])

    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s, NOW(), NOW() )"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)