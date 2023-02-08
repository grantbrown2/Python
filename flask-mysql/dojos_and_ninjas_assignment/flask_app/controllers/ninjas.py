from flask_app import app
from flask import Flask, render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
@app.route('/ninjas')
def Home():
    allNinjas = Ninja.get_ninjas()
    return render_template('index.html', list_all_ninjas = allNinjas)

@app.route('/ninja')
def add_ninja():
    data = {"id":id}
    allDojos = Dojo.get_dojos()
    return render_template('ninja.html', list_all_dojos = allDojos)


# add a ninja route
@app.route('/ninja/add_ninja', methods=['POST'])
def add_ninja_data():
    Ninja.add_ninja(request.form)
    return redirect('/dojo')