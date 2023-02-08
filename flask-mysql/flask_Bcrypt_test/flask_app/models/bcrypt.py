from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL


class Password:
    @classmethod
    def password_test():
        print(generate_password_hash("test"))


# 1. To generate a hash, provide the password to be hashed as an argument
# bcrypt.generate_password_hash(password_string)

# 2.To compare passwords, provide the hash as the first argument and the password to be checked as the second argument
# bcrypt.check_password_hash(hashed_password, password_string)

# Next, when we want to verify a user's password, we'll compare it with the hash we
# have associated with that user in the database. We pass both the hash and the
# provided password to check_password_hash(). Bcrypt extracts the salt from the
# hash and applies it to the provided password, hashes it, and compares the result
# to the saved hash. If they match, it returns True. If not, it returns False.