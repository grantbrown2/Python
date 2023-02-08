from flask_app import app
from flask import Flask, render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
@app.route('/')
def route_redirect():
    return redirect('/dojo')

# home screen/all dojos
@app.route('/dojo')
def all_dojos():
    allDojos = Dojo.get_dojos()
    return render_template('index.html', list_all_dojos = allDojos)

# add a new dojo
@app.route('/dojo/add', methods=["POST"])
def add_dojo():

    # VALIDATION EXAMPLE - WORKS WITH EMAIL EXAMPLE AS WELL
    if not Dojo.validation_dojo(request.form):
        return redirect('/dojo')

    data = {
        "id" : id,
        "dojoName" : request.form['dojoName']
        }
    Dojo.add_dojo(data)
    return redirect('/dojo')

@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    data = {"id" : id}
    return render_template('dojo_show.html', dojo=Dojo.join(data))