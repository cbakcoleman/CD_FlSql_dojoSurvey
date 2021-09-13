from dojoSurvey_app.config.mysqlconnection import connectToMySQL

class Survey:
    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comments = data["comments"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def add_survey( cls, data ):
        query = "INSERT INTO surveys ( name, location, language, comments ) VALUES ( %(name)s, %(location)s, %(language)s, %(comments)s );"
        results = connectToMySQL("dojoSurvey_schema").query_db( query, data )
        return results