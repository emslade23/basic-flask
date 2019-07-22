from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcomePage():
    return render_template("welcome.html")
