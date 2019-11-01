USER_TABLE_NAME = 'user_table'
USER_SCHEMA = {
    'user_id': 'integer PRIMARY KEY',
    'name': 'character(200)'
}

REGION_TABLE_NAME = 'region_table'
REGION_SCHEMA = {
    'region_id': 'integer PRIMARY KEY',
    'region_name': 'character(25)'
}

STATE_TABLE_NAME = 'state_table'
STATE_SCHEMA = {
    'state_id': 'integer PRIMARY KEY',
    'state_name': 'character(25)'
}

INSTANCE_TABLE_NAME = 'instance_table'
INSTANCE_SCHEMA = {
    'instance_id': 'integer PRIMARY KEY',
    'instance_type': 'character(25)'
}

CLUSTER_TABLE_NAME = 'cluster_table'
CLUSTER_SCHEMA = {
    'cluster_id': 'integer PRIMARY KEY',
    'region_id': 'integer',
    'user_id': 'integer',
    'cluster_name': 'character(25) UNIQUE',
    'fk': {
        'region_id': 'region_table(region_id)',
        'user_id': 'user_table(user_id)'
    }
}

MACHINE_TABLE_NAME = 'machine_table'
MACHINE_SCHEMA = {
    'machine_id': 'integer PRIMARY KEY',
    'cluster_id': 'integer',
    'machine_name': 'character(25)',
    'ipaddress': 'character(25) UNIQUE',
    'instance_id': 'integer',
    'state_id': 'integer',
    'fk': {
        'cluster_id': 'cluster_table(cluster_id)',
        'instance_id': 'instance_table(instance_id)',
        'state_id': 'state_table(state_id)'
    }
}

MACHINE_TAGS_TABLE_NAME = 'machine_tags_table'
MACHINE_TAGS_SCHEMA = {
    'tag_id': 'integer PRIMARY KEY',
    'machine_id': 'integer',
    'tag_name': 'character(25)',
    'tag_value': 'character(25)',
    'fk': {
        'machine_id': 'machine_table(machine_id)'
    }
}
