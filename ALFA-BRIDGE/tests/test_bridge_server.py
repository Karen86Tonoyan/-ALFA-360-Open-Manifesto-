import unittest
import sys
import os
from unittest.mock import patch

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bridge_server import app

class TestBridgeServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('psutil.cpu_percent')
    @patch('psutil.virtual_memory')
    @patch('psutil.pids')
    def test_scan_endpoint(self, mock_pids, mock_virtual_memory, mock_cpu_percent):
        # Mock the return values of psutil functions
        mock_cpu_percent.return_value = 50.0
        mock_virtual_memory.return_value.percent = 60.0
        mock_pids.return_value = [1, 2, 3]

        # Send a GET request to the /scan endpoint
        response = self.app.get('/scan')

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response data is the expected JSON
        expected_data = {
            "cpu": 50.0,
            "memory": 60.0,
            "processes": 3
        }
        self.assertEqual(response.get_json(), expected_data)

if __name__ == '__main__':
    unittest.main()
