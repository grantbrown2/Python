from flask import Flask, render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


@app.route('/recipes')
def login_page():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template('recipes.html', recipes=Recipe.join(), user = User.get_user(data))

@app.route('/recipes/new')
def create_recipe():
    if "user_id" not in session:
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods=['POST'])
def add_recipe_to_database():
    if "user_id" not in session:
        return redirect('/')
    if not Recipe.recipe_validation(request.form):
        return redirect('/recipes/new')
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "user_id" : session['user_id']
    }
    Recipe.add_recipe(data)
    return redirect('/recipes')

@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    data = {"id":id}
    Recipe.delete_recipe_from_db(data)
    return redirect('/recipes')


@app.route('/edit_recipe/<int:id>')
def edit_user_get_id(id):
    if "user_id" not in session:
        return redirect('/')
    data = {"id":id}
    return render_template('edit_recipe.html', one_recipe = Recipe.get_recipe(data))

@app.route('/edit_recipe/<int:id>', methods=['POST'])
def edit(id):
    data = {
        "id" : id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions']
    }
    Recipe.edit_recipe_in_db(data)
    return redirect('/recipes')

@app.route('/view_recipe/<int:id>')
def view_recipe(id):
    data = {"id":id}
    return render_template('view_recipe.html', one_recipe = Recipe.get_recipe(data), recipes=Recipe.join())