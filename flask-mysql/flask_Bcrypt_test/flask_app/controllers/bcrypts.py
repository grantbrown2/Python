from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.bcrypt import Password
@app.route('/')
def home():
    Password.password_test()
    return render_template('index.html')