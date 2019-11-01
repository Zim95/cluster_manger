from unittest.mock import patch
from unittest import TestCase

from models import BasePostgresModel


class TestBasePostgresModel(TestCase):

    def test_actual_connection(self):
        base_pg_model = BasePostgresModel()
        connection = base_pg_model.create_connection()
        cursor = base_pg_model.create_cursor(connection)
        
        print(connection)
        print(cursor)
        # self.assertEqual(
        #     connection, 
        # )