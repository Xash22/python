from flask import Flask #importancion del modulo y clase flask

app = Flask (__name__) #creamos la apliacion flaqsh con el constructor de la clase

@app.route("/nombreedad/<nombre>/<edad>") #esta hace referencia a la pagina principal
def nombreedad(nombre,edad): #funcion que contiene el proceso de los que esta debajo
    return f"su nombre es: {nombre} y tiene {edad} anios #devuelve el proceso"
    
    if __name__ == '__main__':
        app.run()          #Ejecuta la aplicacion web
        return f"Hola su nombre"