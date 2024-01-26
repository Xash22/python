
from flask import Flask #importancion del modulo y clase flask

app = Flask (__name__) #creamos la apliacion flaqsh con el constructor de la clase

@app.route("/") #esta hace referencia a la pagina principal
def principal(): #funcion que contiene el proceso de los que esta debajo


def saludar ()
    return "<h2> Aqui esta la pagina principal </h2"


@app.route("/suma/<num1>/<num2>")
def suma(num1,num2):
    resul = num1 + num2
    return f"la suma de {num1} y {num2} es igual {resul}"

if __name__ == '__main__':#
     app.run()