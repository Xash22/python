from flask import Flask, render_template


app = Flask(__name__)

@app.route("/registrate")
def registrate():
    return render_template ("registrate.html")

if __name__ == "__main__":
    app.run(debug=True) 