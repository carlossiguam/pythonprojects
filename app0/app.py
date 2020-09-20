from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('app.html')

@app.route("/about")
def about():
    return "Este sitio web es creado con el fin de palear la no automatizacion existente en la creacion de procesos dentro de la empresa."
if __name__ == "__main__":
    app.run()