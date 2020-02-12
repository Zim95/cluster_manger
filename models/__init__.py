from config import app_settings
import psycopg2


class QueryParser:

    def __init__(self):
        pass


class BasePostgresModel:

    def __init__(
        self, tablename='',
        fields=({},), database=app_settings.POSTGRES_DATABASE
    ):
        self.host = app_settings.POSTGRES_HOST
        self.password = app_settings.POSTGRES_PASSWORD
        self.user = app_settings.POSTGRES_USERNAME
        self.port = app_settings.POSTGRES_PORT

        self.tablename = tablename
        self.database = database
        self.fields = fields[0]

        self.allowed_fields = [
            key for key in self.fields.keys()
        ]

        # for method chaining: for release-v2
        # self.insert_query = ''
        # self.update_query = ''
        # self.get_query = ''
        # self.delete_query = ''

    def create_connection(self):
        connection = psycopg2.connect(
            dbname=self.database,
            password=self.password,
            host=self.host,
            port=self.port,
            user=self.user
        )
        return connection

    def create_cursor(self, connection):
        return connection.cursor()

    def execute_query(self, query):
        try:
            connection = self.create_connection()
            cursor = self.create_cursor(connection)
            cursor.execute(query)
            connection.commit()
            return cursor
        except psycopg2.ProgrammingError as pe:
            connection.rollback()
            raise psycopg2.ProgrammingError(pe)

    def execute_query_list(self, query_list):
        try:
            connection = self.create_connection()
            cursor = self.create_cursor(connection)
            result_list = []
            for query in query_list:
                try:
                    cursor.execute(query)
                    connection.commit()
                    for item in cursor:
                        result_list.append(item)
                except Exception as e:
                    print(e)
                    continue
            return result_list
        except Exception as e:
            connection.rollback()
            raise Exception(e)

    def drop_table(self):
        drop_query = (
            "DROP TABLE {}"
        ).format(
            self.tablename
        )

        # print('Dropping table: {}'.format(drop_query))

        try:
            # connection = self.create_connection()
            # cursor = self.create_cursor(connection)
            # cursor.execute(drop_query)
            # connection.commit()
            self.execute_query(drop_query)
        except Exception as e:
            raise Exception(
                'Could not drop table: {}'.format(
                    str(e)
                )
            )

    def migrate(self):
        if not self.fields or not self.tablename:
            ''' log '''
            return

        ''' Process fields'''
        foregin_keys = {}
        if 'fk' in self.fields:
            foregin_keys = self.fields.pop('fk')

        field_string = ''
        for key, value in self.fields.items():
            field_string += '{key} {value},'.format(
                key=key, value=value
            )

        if foregin_keys:
            for foreign_key, reference in foregin_keys.items():
                field_string += (
                    'FOREIGN KEY({foreign_key}) REFERENCES {reference},'
                ).format(
                    foreign_key=foreign_key,
                    reference=reference
                )

        field_string = field_string[:-1]

        migration_query = (
            "CREATE TABLE IF NOT EXISTS {} ({})"
        ).format(
            self.tablename,
            field_string
        )

        print('Migrating: {}'.format(migration_query))

        try:
            # connection = self.create_connection()
            # cursor = self.create_cursor(connection)
            # cursor.execute(migration_query)
            # connection.commit()
            self.execute_query(migration_query)
        except Exception as e:
            raise Exception(
                'Undefined table error: {}'.format(
                    str(e)
                )
            )

    def check_required(self, record, required=[]):
        record_keys = [key for key in record.keys()]
        required_pass = all(
            [key in required for key in record_keys]
        ) if required else True
        if required_pass:
            return True
        else:
            return False

    def query_parser(self, query_type, record):
        '''
        Description: Formats json into query string
        Usage: 
            base_pg_model.query_parser(
                'insert/update/delete/select/truncate',
                '{
                    json_record    
                }'
            )
        '''
        query_switch = {
            'insert': (
                'INSERT INTO {}.{} ({}) VALUES ({})'
            ).format(
                self.database, self.tablename,
                ','.join(
                    [key for key in record.keys()]
                ),
                ','.join(
                    [
                        "'" + value + "'" if isinstance(
                            value, str
                        ) else value
                        for value in record.values()
                    ]
                )
            ),
            'update': (
                'UPDATE {}.{} {} WHERE {}'.format(
                    self.database, self.tablename,
                    ','.join(
                        [
                            "SET {}={}".format(column, value)
                            for column, value in record.items()
                        ]
                    )
                )
            ),
            'select': (
                'SELECT {} FROM {}.{}'.format(
                    ','.join(record), self.database,
                    self.tablename
                )
            ),
            'delete': (
                'DELETE FROM {}.{} WHERE {}'.format(
                    self.database, self.tablename
                )
            ),
            'truncate': (
                'TRUNCATE {}.{}'.format()
            )
        }
        base_query = query_switch.get(query_type, '')
        if not base_query:
            return ''

        if query_type in ['update', 'delete']:
            where_clause_list = record.get('where')
        else:
            where_clause_list = record.get('where', [])

        where_string = 'WHERE {}'
        where_clause_string_list = []
        for where_clause in where_clause_list:
            column = where_clause.get('column', '')
            operator = where_clause.get('operator', '')
            value = where_clause.get('value', '')
            if not column or not operator or not value:
                continue
            where_clause_string_list.append(
                "{}{}{}" .format(
                    column, operator, value
                )
            )
        where_clause = ' AND '.join(where_clause_string_list)

        query = (
            base_query + where_clause
        ) if where_clause else base_query

        return query

    def insert_one(self, record, required=[]):
        '''
            Description: Inserting a single record to tablename

            Usage:
                model_obj.insert_one(
                    {
                        'column_name': 'value',
                        'column_name': 'value',
                        .....,
                        'where': [
                            {
                                'column': 'column_name',
                                'operator': 'operator_string. eg: >,<,='
                            },
                            {
                                ...
                            },
                            ...
                        ]
                    }
                )

        '''
        if self.check_required(record, required):
            try:
                query = self.query_parser('insert', record)
                self.execute_query(query)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            return False

    def insert_many(self, record_list, required=[]):
        query_list = []
        for record in record_list:
            if self.check_required(record, required):
                try:
                    query = self.query_parser('insert', record)
                    query_list.append(query)
                except Exception as e:
                    print(e)
                    continue
            else:
                continue
        try:
            self.execute_query_list.append(query_list)
            return True
        except Exception as e:
            raise Exception(e)

    def update_one(self, record, required=[]):
        if self.check_required(record, required):
            try:
                query = self.query_parser(
                    'update', record
                )
                return True
            except Exception as e:
                raise Exception(e)

    def update_many(self, record_list, required=[]):
        query_list = []
        for record in record_list:
            if self.check_required(record, required):
                try:
                    # query = self.
                    pass
                except Exception as e:
                    print(e)
                    continue

    def delete_one(self, record, required=[]):
        pass

    def delete_many(self, record_list, required=[]):
        pass

    def get_one(self, record, required=[]):
        pass

    def get_many(self, record_list, required=[]):
        pass
