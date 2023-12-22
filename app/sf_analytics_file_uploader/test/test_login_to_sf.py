import unittest
import requests
from unittest.mock import patch
from xml.etree import ElementTree as ET
from ..src.login_to_sf import login

class TestLogin(unittest.TestCase):

    @patch('requests.post')
    def test_login_successful(self, mock_post):
        # Mock the requests.post method to return a successful response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.content = b"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:partner.soap.sforce.com">
                                       <soapenv:Body>
                                           <urn:loginResponse>
                                               <urn:result>
                                                   <urn:sessionId>mocked_session_id</urn:sessionId>
                                                   <urn:serverUrl>mocked_server_url</urn:serverUrl>
                                               </urn:result>
                                           </urn:loginResponse>
                                       </soapenv:Body>
                                   </soapenv:Envelope>"""

        # Call the login function
        session_id, server_url = login('mocked_username', 'mocked_password', 'mocked_security_token')

        # Check that the function returned the expected values
        self.assertEqual(session_id, 'mocked_session_id')
        self.assertEqual(server_url, 'mocked_server_url')

    @patch('requests.post')
    def test_login_failure(self, mock_post):
        # Mock the requests.post method to raise an exception
        mock_post.side_effect = requests.exceptions.RequestException('Mocked exception')

        # Call the login function
        session_id, server_url = login('mocked_username', 'mocked_password', 'mocked_security_token')

        # Check that the function returned None for both values
        self.assertIsNone(session_id)
        self.assertIsNone(server_url)

if __name__ == '__main__':
    unittest.main()
