from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_users()
    print(users)
    return render_template('read_all.html', all_users = users)

@app.route('/add_user', methods=["POST"])
def add_user():
    data = {
        "id" : id,
        "firstName": request.form['firstName'],
        "lastName": request.form['lastName'],
        "email": request.form['email']
    }

    User.save_user(data)
    return redirect('/')

@app.route('/edit_user/<int:id>', methods=['POST'])
def edit(id):
    data = {
        "id" : id,
        "firstName": request.form['firstName'],
        "lastName": request.form['lastName'],
        "email": request.form['email']
    }
    User.edit_user_info(data)
    return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/read_one/<int:id>')
def read_one(id):
    data = {"id":id}
    return render_template('read_one.html', one_user = User.get_user(data))

@app.route('/edit_user/<int:id>')
def edit_user_get_id(id):
    data = {"id":id}
    return render_template('users_edit.html', one_user = User.get_user(data))

@app.route('/delete_user/<int:id>')
def remove(id):
    data = {"id" : id}
    User.remove_user(data)
    return redirect('/')