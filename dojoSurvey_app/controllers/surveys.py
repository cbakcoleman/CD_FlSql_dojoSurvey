from dojoSurvey_app import app
from flask import render_template, redirect, request
from dojoSurvey_app.models.survey import Survey

@app.route('/')
def home():
    return render_template("index.html", session = session)

@app.route('/store', methods=['POST'])
def store():
    new_survey = Survey.add_survey(request.form)
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template('results.html')