from flask import Flask, render_template
from flaskext.mysql import MySQL 

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='base'

mysql.init_app(app)

@app.route("/")
def index():
    sql = "INSERT INTO `dato` (`id`, `nombre`, `correo`) VALUES (NULL, 'a', 'a@');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template("evaluacion/login.html")


if __name__ == "__main__":
    app.run(debug=True)