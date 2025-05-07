#Core Libraries
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss


#Configure the App
app = Flask(__name__)
Scss(app)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

class CodeProblem(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    priority_level = db.Column(db.Integer, nullable=False)
    pattern_type = db.Column(db.String(30), unique=False, nullable=False)
    notes = db.Column(db.Text, unique=False, nullable=True)