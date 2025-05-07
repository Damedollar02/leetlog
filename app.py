#Core Libraries
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss


#Configure the App
app = Flask(__name__)
Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

#Database Structure (works as a blueprint for the actual db)
class CodeProblem(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    priority_level = db.Column(db.Integer, nullable=False)
    pattern_type = db.Column(db.String(30), unique=False, nullable=False)
    notes = db.Column(db.Text, unique=False, nullable=True)

#Output format for db, useful when debugging 
    def __repr__(self):
        return (
        f"Problem Number: {self.number}, "
        f"Priority: {self.priority_level}, "
        f"Pattern: {self.pattern_type}, "
        f"Notes: {self.notes}"
        )

#Homepage Route
@app.route("/", methods=["POST", "GET"])

def index():
    if request.method == "POST":
        problem_number = request.form.get("number")
        priority = request.form.get("priority")
        pattern = request.form.get("pattern")
        notes = request.form.get("notes")
    else:
        return "HOME"










# Creating the database
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)