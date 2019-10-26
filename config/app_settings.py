import os
from dotenv import load_dotenv


def return_settings():
    ROOT_PATH = os.path.abspath('')
    ENV = os.path.join(ROOT_PATH, '.env')
    load_dotenv(ENV)

    APP_HOST = os.environ.get('APP_HOST', 'localhost')
    APP_PORT = os.environ.get('APP_PORT', 5000)

    POSTGRES_HOST = os.environ.get("POSTGRES_HOST", 'localhost')
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
    POSTGRES_USERNAME = os.environ.get("POSTGRES_USERNAME", 'Namah')
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", 'password123')
    POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE", 'test')

    return {
        'root': ROOT_PATH,
        'env': ENV,
        'app_host': APP_HOST,
        'app_port': APP_PORT,
        'postgres_host': POSTGRES_HOST,
        'postgres_port': POSTGRES_PORT,
        'postgres_username': POSTGRES_USERNAME,
        'postgres_password': POSTGRES_PASSWORD,
        'postgres_database': POSTGRES_DATABASE
    }


settings_dictionary = return_settings()

APP_HOST = settings_dictionary.get('app_host')
APP_PORT = settings_dictionary.get('app_port')

POSTGRES_HOST = settings_dictionary.get('postgres_host')
POSTGRES_PORT = settings_dictionary.get('postgres_port')
POSTGRES_USERNAME = settings_dictionary.get('postgres_username')
POSTGRES_PASSWORD = settings_dictionary.get('postgres_password')
POSTGRES_DATABASE = settings_dictionary.get('postgres_database')
