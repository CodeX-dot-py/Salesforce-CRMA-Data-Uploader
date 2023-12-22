import unittest
import os
import json

from ..src.base64_converter import csv_to_base64, json_to_base64


class TestBase64Converter(unittest.TestCase):

    def setUp(self):
        # Create a temporary JSON file for testing
        self.json_data = {'key': 'value', 'another_key': 'another_value'}
        self.json_file_path = 'test_json_file.json'
        with open(self.json_file_path, 'w') as jsonfile:
            json.dump(self.json_data, jsonfile)

        # Create a temporary CSV file for testing
        self.csv_data = 'name,age\nJohn,25\nDoe,30'
        self.csv_file_path = 'test_csv_file.csv'
        with open(self.csv_file_path, 'w') as csvfile:
            csvfile.write(self.csv_data)

    def tearDown(self):
        # Clean up temporary files after tests
        os.remove(self.json_file_path)
        os.remove(self.csv_file_path)

    def test_json_to_base64(self):
        base64_encoded = json_to_base64(self.json_file_path)
        self.assertIsInstance(base64_encoded, str)
        self.assertNotEqual(base64_encoded, '')

    def test_csv_to_base64(self):
        base64_encoded = csv_to_base64(self.csv_file_path)
        self.assertIsInstance(base64_encoded, str)
        self.assertNotEqual(base64_encoded, '')

if __name__ == '__main__':
    unittest.main()
