from flask import Flask
app = Flask(__name__)
Cal = []

@app.route('/')
def home():
    return "Simple calculator"

@app.route('/add/<a>/<b>')
def addtion(a, b):
    a1 = int(a)
    b1 = int(b)
    c = (a1+b1)
    return str(c)

@app.route("/sub/<a>/<b>")
def sub(a, b):
    a1 = int(a)
    b1 = int(b)
    return "Subtraction:", a1-b1

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
