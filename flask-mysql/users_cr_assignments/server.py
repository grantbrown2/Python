from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from user import User, addUser

@app.route('/')
def index():
    users = User.get_users()
    print(users)
    return render_template('read.html', all_users = users)

@app.route('/add_user', methods=["POST"])
def add_user():
    data = {
        "firstName": request.form['firstName'],
        "lastName": request.form['lastName'],
        "email": request.form['email']
    }
    addUser.saveUser(data)
    return redirect('/')

@app.route('/create')
def Create():
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)