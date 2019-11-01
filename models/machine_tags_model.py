from models import BasePostgresModel
from constants.model_constants import (
    MACHINE_TAGS_SCHEMA, MACHINE_TAGS_TABLE_NAME
)


class MachineTagsModel(BasePostgresModel):

    def __init__(self):
        self.fields = MACHINE_TAGS_SCHEMA,
        self.tablename = MACHINE_TAGS_TABLE_NAME
        super().__init__(
            tablename=self.tablename,
            fields=self.fields
        )
