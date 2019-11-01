from models import BasePostgresModel
from constants.model_constants import MACHINE_SCHEMA, MACHINE_TABLE_NAME


class MachineModel(BasePostgresModel):

    def __init__(self):
        self.fields = MACHINE_SCHEMA,
        self.tablename = MACHINE_TABLE_NAME
        super().__init__(
            tablename=self.tablename,
            fields=self.fields
        )
