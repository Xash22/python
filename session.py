from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def session():
    return render_template("iniciar_session.html")

@app.route("/submit")
def registrate():
    return render_template("registrate.html")



if __name__ == "__main__":
    app.run(debug=True) 