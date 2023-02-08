from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.full_name = data['first_name'] + " " + data['last_name']
        self.email = data['email']
        self.create_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

class addUser:
    @classmethod
    def saveUser(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at ) VALUES (%(firstName)s, %(lastName)s , %(email)s , NOW(), NOW() )"
        return connectToMySQL('users_schema').query_db(query, data)