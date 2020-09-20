from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hola pendejo ilustrado eso es lo que eres"

@app.route("/about")
def about():
    return "Este sitio web es creado con el fin de palear la no automatizacion existente en la creacion de procesos dentro de la empresa."
if __name__ == "__main__":
    app.run()