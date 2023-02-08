from flask import Flask, render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    if not user.User.registration_validation(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash,
        "confirm_password" : request.form['confirm_password']}
    user_id = user.User.create_user(data)
    session['user_id'] = user_id
    return redirect('/recipes')

@app.route('/login', methods=['POST'])
def user_login():
    data = {"email" : request.form["login_email"]}
    user_in_db = user.User.get_email(data)
    if not user_in_db:
        flash(u"Invalid Email/Password", "login_error")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login_password']):
        flash(u"Invalid Email/Password", "login_error")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/recipes")

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')