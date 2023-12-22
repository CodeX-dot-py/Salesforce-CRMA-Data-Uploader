import unittest
from unittest.mock import patch
from ..src.upload import UploadToSfOrg

class TestUploadToSfOrg(unittest.TestCase):

    @patch('requests.post')
    def test_metadata_writer_success(self, mock_post):
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

        # Create an instance of UploadToSfOrg and call the method
        uploader = UploadToSfOrg('mocked_username', 'mocked_password', 'mocked_security_token')
        result = uploader.__metadata_writer('mocked_dataset_alias', 'mocked_crma_app_name', 'mocked_operation_type', 'mocked_data')

        # Check that the method returned the expected value
        self.assertEqual(result, 'mocked_insights_external_data_id')


    @patch('requests.post')
    def test_data_writer_success(self, mock_post):
        # Mock the requests.post method to return a successful response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.content = b"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:partner.soap.sforce.com">
                                       <soapenv:Body>
                                           <urn:createResponse>
                                               <urn:result>
                                                   <urn:id>mocked_insights_external_data_part_id</urn:id>
                                               </urn:result>
                                           </urn:createResponse>
                                       </soapenv:Body>
                                   </soapenv:Envelope>"""

        # Create an instance of UploadToSfOrg and call the method
        uploader = UploadToSfOrg('mocked_username', 'mocked_password', 'mocked_security_token')
        result = uploader.__data_writer('mocked_insights_external_data_id', 'mocked_data')

        # Check that the method returned the expected value
        self.assertEqual(result, 'mocked_insights_external_data_part_id')

    @patch('requests.post')
    def test_build_csv_success(self, mock_post):
        # Mock the requests.post method to return a successful response
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.content = b"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:partner.soap.sforce.com">
                                       <soapenv:Body>
                                           <urn:updateResponse>
                                               <urn:result>
                                                   <urn:success>true</urn:success>
                                               </urn:result>
                                           </urn:updateResponse>
                                       </soapenv:Body>
                                   </soapenv:Envelope>"""

        # Create an instance of UploadToSfOrg and call the method
        uploader = UploadToSfOrg('mocked_username', 'mocked_password', 'mocked_security_token')
        result = uploader.__build_csv('mocked_insights_external_data_id')

        # Check that the method returned success
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
