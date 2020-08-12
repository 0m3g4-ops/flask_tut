#!/usr/bin/python3
from flask import Flask , render_template 

app=Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/")
def parent():
    return render_template("template.html")

@app.route("/about")
def about():
    return render_template("abt.html")

@app.route("/flag")
def flag():
    return "FUCK YOU"

if __name__=="__main__" :
    app.run(debug=True)