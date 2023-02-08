from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello World!"

@app.route('/play')
def levelOne():
    return render_template("index.html", route="level1")

@app.route('/play/<int:num>')
def levelTwo(num):
    return render_template("index.html", route="level2", num = num)

@app.route('/play/<int:num>/<string:color>')
def levelThree(num, color):
    return render_template("index.html", route="level3", num = num, color = color)

if __name__=="__main__":
    app.run(debug=True)
