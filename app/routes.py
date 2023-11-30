from app import app
from flask import render_template

@app.route("/")
@app.route("/shop")
def shop():
    return render_template("shop.html", title="𝓢𝓱𝓸𝓹")

@app.route("/register")
def register():
    return render_template("register.html", title="𝓡𝓮𝓰𝓲𝓼𝓽𝓮𝓻")

@app.route("/login")
def login():
    return render_template("login.html", title="𝓛𝓸𝓰𝓲𝓷")