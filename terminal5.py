from flask import Flask #importancion del modulo y clase flask

app = Flask (__name__) #creamos la apliacion flaqsh con el constructor de la clase

@app.route("/") #esta hace referencia a la pagina principal
def principal(): #funcion que contiene el proceso de los que esta debajo
    return "<h1> Hola, Buenos dias </h1>" #devuelve el proceso

@app.route("/longitud/<nombre>")
def media(nombre):
    nombre1 = len(nombre) #longitud de el nombre de la medida
    return f"Hola su nombre es: {nombre} y la longitud de {nombre1}"

if __name__ == '__main__':
    app.run()          #Ejecuta la aplicacion web