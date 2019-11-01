from models import BasePostgresModel
from constants.model_constants import REGION_SCHEMA, REGION_TABLE_NAME


class RegionModel(BasePostgresModel):

    def __init__(self):
        self.fields = REGION_SCHEMA,
        self.tablename = REGION_TABLE_NAME
        super().__init__(
            tablename=self.tablename,
            fields=self.fields
        )
