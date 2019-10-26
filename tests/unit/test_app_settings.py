from unittest import TestCase
from unittest.mock import patch


class TestAppSettings(TestCase):

    @patch('dotenv.load_dotenv')
    @patch('os.path.abspath', return_value='./testfolder')
    @patch('os.environ.get',
           side_effect=['', '', '', '', '', '', ''])
    def testValues(self, mocked_environ_get, mocked_os_abspath,
                   mocked_load_dotenv):
        '''
            Here we are mocking the flow rather than checking
            the actual values. This is because settings contains
            sensitive information.
        '''
        from config import app_settings
        settings_dictionary = app_settings.return_settings()
        self.assertEqual(
            settings_dictionary.get('root'),
            './testfolder'
        )
        self.assertEqual(
            settings_dictionary.get('env'),
            './testfolder/.env'
        )
        self.assertEqual(
            settings_dictionary.get('app_host'),
            ''
        )
        self.assertEqual(
            settings_dictionary.get('app_port'),
            ''
        )
        self.assertEqual(
            settings_dictionary.get('postgres_host'),
            ''
        )
        self.assertEqual(
            settings_dictionary.get('postgres_port'),
            ''
        )
        self.assertEqual(
            settings_dictionary.get('postgres_username'),
            ''
        )
        self.assertEqual(
            settings_dictionary.get('postgres_password'),
            ''
        )
        self.assertEqual(
            settings_dictionary.get('postgres_database'),
            ''
        )
