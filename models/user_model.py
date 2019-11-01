from models import BasePostgresModel
from constants.model_constants import USER_SCHEMA, USER_TABLE_NAME


class UserModel(BasePostgresModel):

    def __init__(self):
        self.fields = USER_SCHEMA,
        self.tablename = USER_TABLE_NAME
        super().__init__(
            tablename=self.tablename,
            fields=self.fields
        )
