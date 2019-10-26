USER_TABLE = 'user_table'
USER_SCHEMA = {
    'user_id': 'varchar PRIMARY KEY',
    'name': 'varchar'
}

REGION_TABLE_NAME = 'region_table'
REGION_SCHEMA = {
    'region_id': 'int PRIMARY KEY',
    'region_name': 'varchar'
}

CLUSTER_TABLE_NAME = 'cluster_table'
CLUSTER_SCHEMA = {
    'cluster_id': 'int PRIMARY KEY',
    'region_id': 'int FOREIGN KEY region_table.region_id',
    'user_id': 'int FOREIGN KEY user_table.user_id',
    'cluster_name': 'varchar UNIQUE'
}

INSTANCE_TABLE = 'instance_table'
INSTANCE_SCHEMA = {
    'instance_id': 'int PRIMARY KEY',
    'instance_name': 'varchar'
}

STATE_TABLE = 'state_table'
STATE_SCHEMA = {
    'state_id': 'int PRIMARY KEY',
    'state_name': 'varchar'
}

MACHINE_TABLE_NAME = 'machine_table'
MACHINE_SCHEMA = {
    'machine_id': 'int PRIMARY KEY',
    'cluster_id': 'int FOREIGN KEY cluster_table.cluster_id',
    'name': 'varchar',
    'ipaddress': 'varchar UNIQUE',
    'instance_id': 'int FOREIGN KEY instance_table.instance_id',
    'state_id': 'int FOREIGN KEY '
}


MACHINE_TAGS_TABLE_NAME = 'machine_tags_table'
MACHINE_TAGS_SCHEMA = {
    'tag_id': 'int PRIMARY KEY',
    'machine_id': 'int FOREIGN KEY machine_tags_table.id',
    'tag_name': 'varchar',
    'tag_value': 'varchar'
}