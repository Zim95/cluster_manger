from config import app_settings


class BasePostgresModel:

    def __init__(self, fields={}):
        self.host = app_settings.POSTGRES_HOST
        self.password = app_settings.POSTGRES_PASSWORD
        self.user = app_settings.POSTGRES_USER
        self.database = app_settings.POSTGRES_DATABASE
        self.fields = fields
        self.allowed_fields = [
            key for key in fields.keys()
        ]

    def create_connector(self):
        pass

    def create_cursor(self, cursor):
        pass

    def execute_single_query(self, query):
        pass

    def execute_multiple_queries(self, query):
        pass

    def migrate(self, query):
        if not self.fields:
            return
