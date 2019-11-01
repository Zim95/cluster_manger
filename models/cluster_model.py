from models import BasePostgresModel
from constants.model_constants import CLUSTER_SCHEMA, CLUSTER_TABLE_NAME


class ClusterModel(BasePostgresModel):

    def __init__(self, fields={}):
        self.fields = CLUSTER_SCHEMA,
        self.tablename = CLUSTER_TABLE_NAME
        super().__init__(
            tablename=self.tablename,
            fields=self.fields
        )
