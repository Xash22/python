from flask import Flask #importancion del modulo y clase flask

app = Flask (__name__) #creamos la apliacion flaqsh con el constructor de la clase

@app.route("/") #esta hace referencia a la pagina principal
def principal(): #funcion que contiene el proceso de los que esta debajo
    return "<h1> Hola, Buenos dias </h1>" #devuelve el proceso

@app.route("/adios") #esta hace referencia a la pagina principal
def adios(): #funcion que contiene el proceso de los que esta debajo
    return "<h1> adios hasta la proxima </h1>" #devuelve el proceso

if __name__ == '__main__':
    app.run()          #Ejecuta la aplicacion web