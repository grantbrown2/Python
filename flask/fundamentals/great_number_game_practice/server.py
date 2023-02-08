from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'password'

@app.route('/')
def homeScreen():
    import random
    session['randomNum'] = random.randint(1, 100)
    print(session['randomNum'])
    return render_template("index.html"), session['randomNum']

@app.route('/guess', methods=['POST'])
def findRoute():
    x = int(request.form['guess'])
    y = session['randomNum']
    if x < y:
        return render_template("index.html", validation = "low"), session['randomNum']
    if x > y:
        return render_template("index.html", validation = "high"), session['randomNum']
    if x == y:
        return render_template("index.html", validation = "correct"), session['randomNum']

@app.route('/root')
def addRandomNum():
    import random
    session['randomNum'] = random.randint(1, 100)
    print(session['randomNum'])
    return redirect('/'), session['randomNum']

if __name__ == ("__main__"):
    app.run(debug=True)