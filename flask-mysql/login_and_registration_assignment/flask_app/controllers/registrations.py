from flask import Flask, render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.registration import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/add/user', methods=['POST'])
def add_user():
    if not User.registration_validation(request.form):#name validations
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash,
        "confirm_password" : request.form['confirm_password']}
    user_id = User.add_user(data)
    session['user_id'] = user_id
    return redirect('/')

@app.route('/login', methods=['POST'])
def user_login():
    data = {"email" : request.form["login_email"]}
    user_in_db = User.get_email(data)
    if not user_in_db:
        flash(u"Invalid Email/Password", "login_error")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login_password']):
        flash(u"Invalid Email/Password", "login_error")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/success")

@app.route('/success')
def login_page():
    if "user_id" not in session:
        return redirect('/')
    data = {"id":session['user_id']}
    return render_template('login.html', user = User.get_user_id(data))

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')