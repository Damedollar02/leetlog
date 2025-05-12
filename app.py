#Core Libraries
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from openai import OpenAI
import os
from dotenv import load_dotenv

#Configure the App
app = Flask(__name__)
Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#Database Structure (works as a blueprint for the actual db)
class CodeProblem(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    priority_level = db.Column(db.Integer, nullable=False)
    pattern_type = db.Column(db.String(30), unique=False, nullable=False)
    notes = db.Column(db.Text, unique=False, nullable=True)

#Output format for db, useful when debugging 
    def __repr__(self):
        return (
        f"Problem Number: {self.number}\n"
        f"Priority: {self.priority_level}\n"
        f"Pattern: {self.pattern_type}\n"
        )

#Homepage Route
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        problem_number = int(request.form.get("number"))
        priority = int(request.form.get("priority"))
        pattern = request.form.get("pattern")
        notes = request.form.get("notes")

        new_problem = CodeProblem(
            number = problem_number,
            priority_level = priority,
            pattern_type = pattern,
            notes = notes,
        )
        try:
            db.session.add(new_problem)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "There was an issue adding your leetcode problem"
    else:
        problems = CodeProblem.query.order_by(CodeProblem.priority_level).all()
        return render_template("index.html", problems=problems)
    
#delete record from db
@app.route("/delete/<int:number>", methods=["POST"])
def delete(number):
    record_to_delete = CodeProblem.query.get_or_404(number)
    try:
        db.session.delete(record_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return "There was an issue deleting the problem"

# edit record FIX ME
@app.route("/update/<int:number>", methods=["POST"])
def update(number):
    record_to_update = CodeProblem.query.get_or_404(number)
    
    result = validate_form_types(request.form, record_to_update)

    if result is not True:
        return result
    
    db.session.commit()


def validate_form_types(form_data, problem_record):
    try:
        problem_number = int(form_data.get("number"))
        priority = int(form_data.get("priority"))
        pattern = form_data.get("pattern")
        notes = form_data.get("notes")

        if not pattern:
            raise ValueError("Pattern is required.")

        problem_record.number = problem_number
        problem_record.priority_level = priority
        problem_record.pattern_type = pattern
        problem_record.notes = notes

        return True

    except (ValueError, TypeError) as e:
        return f"Validation error: {e}"



    


@app.route("/analyze", methods=["POST"])
def analyze():
    problems = CodeProblem.query.all()

    if not problems:
        return render_template(
            "index.html",
            problems=problems,
            summary="No problems to analyze. Please add some first."
        )

    problem_list = []

    for problem in problems:
        problem_list.append(
            f"Problem #{problem.number}: Priority Level : {problem.priority_level} Pattern : {problem.pattern_type}"
        )

    ai_input = (
    "Here is a list of LeetCode problems I've stored to review.\n"
    "A higher priority indicates I'm having a harder time solving the problem.\n"
    "Analyze my strengths, weaknesses, and what I should focus on. Be concise.\n"
    "Here's the list:\n" +
    "\n".join(problem_list)
)


    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages =[
            {"role": "user", "content": ai_input}
        ]
    )
    summary = response.choices[0].message.content
    return render_template("index.html", problems=problems, summary=summary)














# Creating the database
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)