# builtins
from unittest.mock import patch
from unittest import TestCase
import json

# module
import app


class TestApiEndpointCluster(TestCase):

    def setUp(self):
        self.app_test_client = app.flask_app.test_client()

    def test_endpoint_functionality(self):
        ''' Testing response code for alerts'''
        resp_get = self.app_test_client.get('/cluster')
        self.assertEqual(resp_get.status_code, 200)
        resp_post = self.app_test_client.post('/cluster')
        self.assertEqual(resp_post.status_code, 200)
        resp_put = self.app_test_client.put('/cluster')
        self.assertEqual(resp_put.status_code, 200)
        resp_delete = self.app_test_client.delete('/cluster')
        self.assertEqual(resp_delete.status_code, 200)

    @patch('apis.Cluster.get',
           return_value={"mocked_response": "mocked_hello"})
    def test_cluster_get_basic(self, mocked_get):
        ''' Test a basic get setup '''
        # check call by using mock return value
        resp_mock = self.app_test_client.get('/cluster')
        mocked_get.assert_called_with()
        self.assertEqual(
            json.loads(resp_mock.get_data().decode('utf-8')),
            {"mocked_response": "mocked_hello"}
        )

    @patch('apis.Cluster.post',
           return_value={"mocked_response": "mocked_hello"})
    def test_cluster_post_basic(self, mocked_post):
        ''' Test a basic post setup '''
        resp_mock = self.app_test_client.post('/cluster')
        mocked_post.assert_called_with()
        self.assertEqual(
            json.loads(resp_mock.get_data().decode('utf-8')),
            {"mocked_response": "mocked_hello"}
        )

    @patch('apis.Cluster.put',
           return_value={"mocked_response": "mocked_hello"})
    def test_cluster_put_basic(self, mocked_put):
        ''' Test a basic put setup '''
        resp_mock = self.app_test_client.put('/cluster')
        mocked_put.assert_called_with()
        self.assertEqual(
            json.loads(resp_mock.get_data().decode('utf-8')),
            {"mocked_response": "mocked_hello"}
        )

    @patch('apis.Cluster.delete',
           return_value={"mocked_response": "mocked_hello"})
    def test_cluster_delete_basic(self, mocked_delete):
        ''' Test a basic delete setup '''
        resp_mock = self.app_test_client.delete('/cluster')
        mocked_delete.assert_called_with()
        self.assertEqual(
            json.loads(resp_mock.get_data().decode('utf-8')),
            {"mocked_response": "mocked_hello"}
        )


class TestApiEndpointMachine(TestCase):

    def setUp(self):
        self.app_test_client = app.flask_app.test_client()

    def test_endpoint_functionality(self):
        ''' Testing response code for alerts'''
        resp_get = self.app_test_client.get('/machine')
        self.assertEqual(resp_get.status_code, 200)
        resp_post = self.app_test_client.post('/machine')
        self.assertEqual(resp_post.status_code, 200)
        resp_put = self.app_test_client.put('/machine')
        self.assertEqual(resp_put.status_code, 200)
        resp_delete = self.app_test_client.delete('/machine')
        self.assertEqual(resp_delete.status_code, 200)

    @patch('apis.Machine.get',
           return_value={"mocked_response": "mocked_hello"})
    def test_cluster_get_basic(self, mocked_get):
        ''' Test a basic get setup '''
        # check call by using mock return value
        resp_mock = self.app_test_client.get('/machine')
        mocked_get.assert_called_with()
        self.assertEqual(
            json.loads(resp_mock.get_data().decode('utf-8')),
            {"mocked_response": "mocked_hello"}
        )

    @patch('apis.Machine.post',
           return_value={"mocked_response": "mocked_hello"})
    def test_cluster_post_basic(self, mocked_post):
        ''' Test a basic post setup '''
        resp_mock = self.app_test_client.post('/machine')
        mocked_post.assert_called_with()
        self.assertEqual(
            json.loads(resp_mock.get_data().decode('utf-8')),
            {"mocked_response": "mocked_hello"}
        )

    @patch('apis.Machine.put',
           return_value={"mocked_response": "mocked_hello"})
    def test_cluster_put_basic(self, mocked_put):
        ''' Test a basic put setup '''
        resp_mock = self.app_test_client.put('/machine')
        mocked_put.assert_called_with()
        self.assertEqual(
            json.loads(resp_mock.get_data().decode('utf-8')),
            {"mocked_response": "mocked_hello"}
        )

    @patch('apis.Machine.delete',
           return_value={"mocked_response": "mocked_hello"})
    def test_cluster_delete_basic(self, mocked_delete):
        ''' Test a basic delete setup '''
        resp_mock = self.app_test_client.delete('/machine')
        mocked_delete.assert_called_with()
        self.assertEqual(
            json.loads(resp_mock.get_data().decode('utf-8')),
            {"mocked_response": "mocked_hello"}
        )
