from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/enlace1")
def pagina3():
    return render_template("pag.html")


@app.route("/enlace2")
def pagina4():
    return render_template("pag.html")


@app.route("/formulario")
def formulario():
    return render_template("app3for.html")


@app.route("/gracias")
def gracias():
    valor1 = request.args.get('nombre') #input de formulario nombre
    valor2 = request.args.get('apellidos') # input edad del formurio
    return render_template("app2.html",nombre=valor1,apellidos=valor2) # nombre va en el valor 1 y edad en el valor 2 de los input

if __name__ == '__main__':
    app.run(debug=True)