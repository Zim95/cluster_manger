# builtins
import unittest
from unittest.mock import patch

# third party
from flask import Flask
from flask_restful import Api

# module
import app


class TestApp(unittest.TestCase):

    def test_app_creation(self):
        ''' check if app has correctly been instantiated '''
        self.assertEqual(
           isinstance(app.flask_app, Flask),
           True
        )

        ''' check if __name__ for app is app'''
        self.assertEqual(
            vars(app).get('__name__', ''),
            'app'
        )

        ''' check if import_name for flask_app is app'''
        self.assertEqual(
            vars(app.flask_app).get('import_name', ''),
            'app'
        )

        ''' check if API has been correctly instantiated '''
        self.assertEqual(
            isinstance(app.api, Api),
            True
        )

        ''' check if the run method is being executed when name is main'''
        ''' Not a major test, but just to make sure '''
        ''' things are under our control'''


if __name__ == "__main__":
    unittest.main()
