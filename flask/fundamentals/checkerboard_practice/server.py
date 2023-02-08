from flask import Flask, render_template
app = Flask(__name__)

# Home screen default 8x8 checkerboard
@app.route('/')
def checkerBoard():
    return render_template("index.html", board = "default")
# Custom Y checkerboard
@app.route('/<int:numY>')
def checkerBoard2(numY):
    return render_template("index.html", board = "customSize", numY = numY)
# Custom X & Y checkerboard
@app.route('/<int:numY>/<int:numX>')
def checkerBoard3(numY, numX):
    return render_template("index.html", board = "customSize2", numY = numY, numX = numX)
# Custom X & Y checkerboard with custom colors
@app.route('/<int:numY>/<int:numX>/<string:customColor1>/<string:customColor2>')
def checkerBoard4(numY, numX, customColor1, customColor2):
    return render_template("index.html", board = "customSize3", numY = numY, numX = numX, customColor1 = customColor1, customColor2 = customColor2)

if __name__=="__main__":
    app.run(debug=True)
