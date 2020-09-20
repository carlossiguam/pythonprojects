from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hola pendejo ilustrado eso es lo que eres"

if __name__ == "__main__":
    app.run()