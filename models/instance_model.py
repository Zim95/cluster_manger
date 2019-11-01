from models import BasePostgresModel
from constants.model_constants import INSTANCE_SCHEMA, INSTANCE_TABLE_NAME


class InstanceModel(BasePostgresModel):

    def __init__(self):
        self.fields = INSTANCE_SCHEMA,
        self.tablename = INSTANCE_TABLE_NAME
        super().__init__(
            tablename=self.tablename,
            fields=self.fields
        )
