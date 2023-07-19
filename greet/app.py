from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome/<where>")
def welcome(where):
    return f"welcome {where}"
    
@app.route("/welcome")
def baseWelcome():
    return "welcome"
 
@app.route("/")
def home():
    return "homepage found"