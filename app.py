from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = (
    "mongodb+srv://vyshnav:vyshnav@cluster0.pm7ru69.mongodb.net/test?retryWrites=true&w=majority&appName=Cluster0"
)
mongo = PyMongo(app)


@app.route("/")
def index():
    return "hello"


@app.route("/<name>", methods=["GET", "POST"])
def printname(name):
    if request.method == "POST":
        # If it's a POST request, insert the provided name into the database

        mongo.db.student.insert_one({"name": name})
        return "Name {} inserted successfully.".format(name)

    else:
        # If it's a GET request, retrieve the specified name from the database
        student = mongo.db.student.find_one({"name": name})
        if student:
            return "Hello, my name is {}.".format(student["name"])
        else:
            return "Name not found in the database."


@app.route("/hi/get_all_details", methods=["GET"])
def get_all_details():
    try:
        # Retrieve all documents from the 'student' collection
        students = list(mongo.db.student.find({}, {"_id": False, "name": True}))

        # Check if any documents are found
        if students:
            # If documents are found, return them as JSON
            return jsonify(students)
        else:
            # If no documents are found, return a message
            return "No documents found in the collection."
    except Exception as e:
        # Log the exception for debugging purposes
        print("An error occurred:", str(e))
        # Return a generic error message
        return f"An error occurred while processing your request.{str(e)}", 500
