from flask_app.config.mysqlconnection import connectToMySQL




class User:
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        return connectToMySQL("mydb").mysql.query_db(query, data)