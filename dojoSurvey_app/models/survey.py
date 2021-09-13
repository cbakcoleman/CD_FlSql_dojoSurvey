from dojoSurvey_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comments = data["comments"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey["name"]) < 3:
            flash("Name must be at least 3 characters.", "name")
            is_valid = False
        return is_valid

    @classmethod
    def add_survey( cls, data ):
        query = "INSERT INTO surveys ( name, location, language, comments ) VALUES ( %(name)s, %(location)s, %(language)s, %(comments)s );"
        results = connectToMySQL("dojoSurvey_schema").query_db( query, data )
        return results

    @classmethod
    def all_surveys( cls ):
        query = "SELECT * FROM surveys;"
        results = connectToMySQL("dojoSurvey_schema").query_db( query )
        all_surveys = []
        for row in results:
            all_surveys.append( cls(row) )
        return all_surveys