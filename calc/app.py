from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/")
def default():
    return "Flask is loading correctly"
    
@app.route("/add")
def display_add():
    return str(add(int(request.args["a"]), int(request.args["b"])))
    
@app.route("/sub")
def display_sub():
    return str(sub(int(request.args["a"]), int(request.args["b"])))
    
@app.route("/div")
def display_div():
    return str(div(int(request.args["a"]), int(request.args["b"])))
    
@app.route("/mult")
def display_mult():
    return str(mult(int(request.args["a"]), int(request.args["b"])))