from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'password'
# This was a very tough assignment for me
@app.route('/')
def view_counter():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def add_count():
    session['count'] = 0
    return redirect('/')

@app.route('/addCount2')
def view_counter2():
    session["count"] += 1
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)