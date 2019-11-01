from unittest import TestCase
from unittest.mock import patch, MagicMock

# third party
from models import BasePostgresModel
from config import app_settings
import psycopg2

    
class TestBaseModel(TestCase):

    def setUp(self):
        self.base_postgres_model = BasePostgresModel()
        with patch('psycopg2.connect') as mock_connect:
            self.mock_connect = psycopg2.connect()
            self.mock_connect.commit = mock_connect.commit
            self.mock_connect.cursor = mock_connect.cursor
            self.mock_connect.cursor.execute = mock_connect.cursor.execute

    def test_initialization(self):
        ''' Check for constant values'''
        self.assertEqual(
            self.base_postgres_model.host,
            app_settings.POSTGRES_HOST
        )
        self.assertEqual(
            self.base_postgres_model.password,
            app_settings.POSTGRES_PASSWORD
        )
        self.assertEqual(
            self.base_postgres_model.database,
            app_settings.POSTGRES_DATABASE
        )
        self.assertEqual(
            self.base_postgres_model.user,
            app_settings.POSTGRES_USERNAME
        )
        self.assertEqual(
            self.base_postgres_model.port,
            app_settings.POSTGRES_PORT
        )

        ''' Check for parameterized values'''
        self.assertEqual(
            self.base_postgres_model.tablename,
            ''
        )
        self.assertEqual(
            self.base_postgres_model.fields,
            {}
        )
        self.assertEqual(
            self.base_postgres_model.allowed_fields,
            []
        )

    @patch('psycopg2.connect')
    def test_create_connection(self, mock_connection):
        '''
        We have used mock to avoid actual connection call.
        The actual connection takes some time.
        '''
        connection = self.base_postgres_model.create_connection()
        mock_connection.assert_called_with(
            dbname=self.base_postgres_model.database,
            host=self.base_postgres_model.host,
            password=self.base_postgres_model.password,
            port=self.base_postgres_model.port,
            user=self.base_postgres_model.user
        )

    @patch('psycopg2.connect.cursor')
    @patch('psycopg2.connect')
    def test_create_cursor(self, mock_connection, mock_cursor):
        '''
        We will use a mock to avoid actual connection
        '''
        cursor = self.base_postgres_model.create_cursor(mock_connection)
        mock_cursor.assert_called_with()

    @patch('models.BasePostgresModel.create_cursor')
    @patch('models.BasePostgresModel.create_connection', return_value='x')
    def test_execute_query(self, mock_create_connection, mock_create_cursor):
        result = self.base_postgres_model.execute_query('x')

        mock_create_connection.assert_called_with()
        mock_create_cursor.assert_called_with('x')

        '''
        Why use result?
        --> when we run execute_query, we get a mock
            which is the create_cursor mock
            In call execution,
                (result of create_cursor).execute is called
            Therefore, this logic worked
        '''
        result.execute.assert_called_with('x')

    def test_drop_table(self):
        '''
            Here we test if the functions are called properly.
            The reason we don't go into the exception block is
            because we have done everything accordingly.

            The only way this block will fail is if our
            connections fail.
            In which case, this test would fail and we would
            be notified right away
        '''
        connect = self.mock_connect
        with patch(
            'models.BasePostgresModel.create_cursor'
        ) as mock_cursor:
            with patch('models.BasePostgresModel.create_connection',
                       return_value=connect) as mock_connection:
                self.base_postgres_model.drop_table()
                mock_connection.assert_called_with()
                mock_cursor.assert_called_with(connect)
                mock_cursor().execute.assert_called_with(
                    "DROP TABLE "
                )
                connect.commit.assert_called_with()

    def test_migrate(self):
        self.base_postgres_model.migrate()