from models import BasePostgresModel
from constants.model_constants import STATE_SCHEMA, STATE_TABLE_NAME


class StateModel(BasePostgresModel):

    def __init__(self):
        self.fields = STATE_SCHEMA,
        self.tablename = STATE_TABLE_NAME
        super().__init__(
            tablename=self.tablename,
            fields=self.fields
        )
