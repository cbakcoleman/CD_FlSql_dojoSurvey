from dojoSurvey_app import app
from flask import render_template, redirect, request
from dojoSurvey_app.models.survey import Survey

@app.route('/')
def home():
    return render_template("survey.html")

@app.route('/store', methods=['POST'])
def store():
    if not Survey.validate_survey(request.form):
        return redirect()
    new_survey = Survey.add_survey( request.form)
    return redirect('/results')

@app.route('/results')
def show_results():
    all_surveys = Survey.all_surveys()
    return render_template('results.html', surveys = all_surveys)