import os
from datetime import datetime

import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from dotenv import find_dotenv, load_dotenv
from flask import Flask, Response, request

load_dotenv(find_dotenv())

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGODB_URI")
assert MONGODB_URI
client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]  # accessing the database


@app.route("/api/v1.0/students", methods=["GET"])
def students():
    students = db.students.find()
    return Response(dumps(students), mimetype="application/json")


@app.route("/api/v1.0/students/<id>", methods=["GET"])
def single_student(id):
    student = db.students.find({"_id": ObjectId(id)})
    return Response(dumps(student), mimetype="application/json")


@app.route("/api/v1.0/students", methods=["POST"])
def create_student():
    name = request.form.get("name")
    country = request.form.get("country")
    city = request.form.get("city")
    skills = [skill.strip() for skill in request.form.get("skills", "").split(",")]
    bio = request.form.get("bio")
    birthyear = request.form.get("birthyear")
    created_at = datetime.now()
    student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": skills,
        "bio": bio,
        "created_at": created_at,
    }
    db.students.insert_one(student)
    return Response(dumps({"result": "student created"}), mimetype="application/json")


@app.route("/api/v1.0/students/<id>", methods=["PUT"])
def update_student(id: str):
    query = {"_id": ObjectId(id)}
    name = request.form.get("name")
    country = request.form.get("country")
    city = request.form.get("city")
    skills: list[str] = request.form.get("skills", "").split(", ")
    bio = request.form.get("bio")
    birthyear = request.form.get("birthyear")
    student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": [skill.strip() for skill in skills],
        "bio": bio,
    }
    db.students.update_one(query, {"$set": student})
    return Response(
        dumps({"result": "a new student has beencreated"}), mimetype="application/json"
    )
    # return


@app.route("/api/v1.0/students/<id>", methods=["DELETE"])
def delete_student(id: str):
    db.students.delete_one({"_id": ObjectId(id)})
    return Response(
        dumps({"result": "student was deleted"}), mimetype="application/json"
    )


if __name__ == "__main__":
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
