from flask import Flask, render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.sasquatch import Sasquatch
from flask_app.models.user import User


@app.route('/sasquatch/new')
def create_sasquatch_sighting():
    if "user_id" not in session:
        return redirect('/')
    data = {"id":session['user_id']}
    return render_template('create_sighting.html', user = User.get_user_id(data))

@app.route('/sasquatch/create', methods=['POST'])
def add_sasquatch_to_database():
    if "user_id" not in session:
        return redirect('/')
    if not Sasquatch.sasquatch_validation(request.form):
        return redirect('/sasquatch/new')
    data = {
        "location" : request.form['location'],
        "what_happened" : request.form['what_happened'],
        "date_seen" : request.form['date_seen'],
        "count" : request.form['count'],
        "user_id" : session['user_id']
    }
    Sasquatch.add_sasquatch(data)
    return redirect('/dashboard')

@app.route('/edit_sasquatch/<int:id>')
def edit_sasquatch_get_id(id):
    if "user_id" not in session:
        return redirect('/')
    data = {"id":id}
    login_data = {"id":session['user_id']}
    return render_template('edit_sasquatch.html', one_sasquatch = Sasquatch.get_sasquatch(data), user = User.get_user_id(login_data))

@app.route('/edit_sasquatch/<int:id>', methods=['POST'])
def edit(id):
    if not Sasquatch.sasquatch_validation(request.form):
        return redirect('/sasquatch/new')
    data = {
        "id" : id,
        "location": request.form['location'],
        "what_happened": request.form['what_happened'],
        "date_seen": request.form['date_seen'],
        "count": request.form['count']
    }
    Sasquatch.edit_sasquatch_in_db(data)
    return redirect('/dashboard')

@app.route('/delete_sasquatch/<int:id>')
def delete_recipe(id):
    data = {"id":id}
    Sasquatch.delete_sasquatch_from_db(data)
    return redirect('/dashboard')

@app.route('/view_sasquatch/<int:id>')
def view_recipe(id):
    data = {"id":id}
    login_data = {"id":session['user_id']}
    return render_template('view_sasquatch.html', one_sasquatch = Sasquatch.get_sasquatch(data), sasquatch = Sasquatch.join(), user = User.get_user_id(login_data))
