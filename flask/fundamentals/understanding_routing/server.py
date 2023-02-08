from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello World!"

@app.route('/dojo')
def sayDojo():
    return "Dojo!"

@app.route('/say/<string:say>')
def saySomething(say):
    return "Hi " + say + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    return word * num

if __name__=="__main__":
    app.run(debug=True)


