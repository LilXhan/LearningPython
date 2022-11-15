from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    user = {
        "nombre": "Flavio",
        "apellido": "Alvarado",
        "telefono": "979960088"
    }

    """
        DESTRUCTURAMOS
    """

    return render_template("index.html", **user) # key=value

@app.route("/ruta-nueva-1")
def ruta_nueva():
    return "Hola Mundo"

@app.route("/ruta-nueva-1/ruta-html")
def ruta_nueva_html():
    return render_template("ruta.html")


hello_world()



