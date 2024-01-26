from flask import Flask, render_template
from flaskext.mysql import MySQL # definiendo que se utiliza parte del modulo sql

app = Flask(_name_)

####### Declarando el uso de mysql #########

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # Donde se encuentra esa base de datos o ruta
app.config['MYSQL_DATABASE_USER'] = 'root' # Usario
app.config['MYSQL_DATABASE_PASSWORD']='' # La contraseña
app.config['MYSQL_DATABASE_DB']='estudiante' #    El nombre de la base de datos  
mysql.init_app(app) # Esta es para la iniciar la coneccion 

@app.route("/")
def index():

        sql=""
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()
         return render_template("empleados/index.html")

@app.route("/create")
def create():
        return render_template(empleado/create.html)
 
if _name_ == 'main':