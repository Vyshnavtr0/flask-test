from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def index():

    return "hello"


@app.route("/<name>")
def printname(name):
    return "hello my name is{}".format(name)
