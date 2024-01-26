from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def principal(): # funcion llamada principal
    return render_template("app_1_index.html") 

@app.route("/variables")
def variables():
    valor = "Antonio"
    valor_edad = 35
    return render_template("app_1_variables.html", nombre=valor,edad=valor_edad)

if __name__== '__main__':
    app.run(debug=True)