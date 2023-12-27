import requests
import xml.etree.ElementTree as ET
from .login_to_sf import login
from .base64_converter import csv_to_base64, json_to_base64

class UploadToSfOrg:
    """
    A class for uploading data to Salesforce using the SOAP API.

    Parameters:
    - username (str): Salesforce username.
    - password (str): Salesforce password.
    - security_token (str): Salesforce security token.
    """
    def __init__(self, username: str, password: str, security_token: str) -> None:
        """
        Initialize the UploadToSfOrg instance.

        Retrieves the session ID and SOAP URL using Salesforce login.

        Parameters:
        - username (str): Salesforce username.
        - password (str): Salesforce password.
        - security_token (str): Salesforce security token.
        """
        self.session_id, self.soap_url = login(username, password, security_token)
        self.soap_header = {
            'content-type': 'text/xml',
            'charset': 'UTF-8',
            'SOAPAction': '""'
        }

    def __send_soap_request(self, request_template:str, *args):
        """
        Send a SOAP request to Salesforce.

        Parameters:
        - request_template (str): The SOAP request template.
        - *args: Arguments to format the SOAP request.

        Returns:
        - Response: The response from the SOAP request.
        """
        soap_request = request_template.format(self.session_id, *args)
        try:
            response = requests.post(url=self.soap_url, data=soap_request, headers=self.soap_header)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error in SOAP request: {e}")
            return None

    def __metadata_writer(self, dataset_alias:str, crma_app_name:str, upload_operation_type:str, data:str):
        """
        Write metadata to Salesforce.

        Parameters:
        - dataset_alias (str): Alias of the dataset.
        - crma_app_name (str): Name of the CRM Analytics app.
        - upload_operation_type (str): Type of upload operation.
        - data (str): Metadata in base64-encoded format.

        Returns:
        - str: Insights External Data ID.
        """
        request_template = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:partner.soap.sforce.com" xmlns:urn1="urn:sobject.partner.soap.sforce.com">
                <soapenv:Header>
                    <urn:SessionHeader>
                        <urn:sessionId>{}</urn:sessionId>
                    </urn:SessionHeader>
                </soapenv:Header>
                <soapenv:Body>
                    <urn:create>
                        <urn:sObjects>
                            <urn:type>InsightsExternalData</urn:type>
                            <urn:EdgemartAlias>{}</urn:EdgemartAlias>
                            <urn:EdgemartContainer>{}</urn:EdgemartContainer>
                            <urn:Format>Csv</urn:Format>
                            <urn:Operation>{}</urn:Operation>
                            <urn:Action>None</urn:Action>
                            <urn:MetadataJson>{}</urn:MetadataJson>
                        </urn:sObjects>
                    </urn:create>
                </soapenv:Body>
            </soapenv:Envelope>
        """
        response = self.__send_soap_request(request_template, dataset_alias, crma_app_name, upload_operation_type, data)
        if response is not None:
            root = ET.fromstring(response.content)
            insights_external_data_id = root.find('.//{urn:partner.soap.sforce.com}id').text
            return insights_external_data_id
        else:
            return None

    def __data_writer(self, insights_external_data_id:str, data:str):
        """
        Write data to Salesforce.

        Parameters:
        - insights_external_data_id (str): Insights External Data ID.
        - data (str): Data in base64-encoded format.

        Returns:
        - Response: The response from the SOAP request.
        """
        request_template = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:partner.soap.sforce.com" xmlns:urn1="urn:sobject.partner.soap.sforce.com">
                <soapenv:Header>
                    <urn:SessionHeader>
                        <urn:sessionId>{}</urn:sessionId>
                    </urn:SessionHeader>
                </soapenv:Header>
                <soapenv:Body>
                    <urn:create>
                        <urn:sObjects>
                            <urn:type>InsightsExternalDataPart</urn:type>
                            <urn:PartNumber>1</urn:PartNumber>
                            <urn:InsightsExternalDataId>{}</urn:InsightsExternalDataId>
                            <urn:DataFile>{}</urn:DataFile>
                        </urn:sObjects>
                    </urn:create>
                </soapenv:Body>
            </soapenv:Envelope>
        """
        response = self.__send_soap_request(request_template, insights_external_data_id, data)
        return response

    def __build_csv(self, insights_external_data_id:str):
        """
        Build CSV in Salesforce.

        Parameters:
        - insights_external_data_id (str): Insights External Data ID.

        Returns:
        - Response: The response from the SOAP request.
        """
        request_template = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:partner.soap.sforce.com" xmlns:urn1="urn:sobject.partner.soap.sforce.com">
                <soapenv:Header>
                    <urn:SessionHeader>
                        <urn:sessionId>{}</urn:sessionId>
                    </urn:SessionHeader>
                </soapenv:Header>
                <soapenv:Body>
                    <urn:update>
                        <urn:sObjects>
                            <urn:type>InsightsExternalData</urn:type>
                            <urn:Id>0{}</urn:Id>
                            <urn:Action>Process</urn:Action>
                        </urn:sObjects>
                    </urn:update>
                </soapenv:Body>
            </soapenv:Envelope>
        """
        response = self.__send_soap_request(request_template, insights_external_data_id)
        return response

    def write_to_crma_app(self, crma_app_alias:str, dataset_alias:str,
                           local_dataset_path:str, local_dataset_metadata_path:str, 
                           data_operation_type:str):
        """
        Write data to a Salesforce CRM Analytics app.

        Parameters:
        - crma_app_alias (str): Alias of the CRM Analytics app.
        - dataset_alias (str): Alias of the dataset.
        - local_dataset_path (str): Local path of the dataset file.
        - local_dataset_metadata_path (str): Local path of the dataset metadata file.
        - data_operation_type (str): Type of data operation.

        Returns:
        - Response: The response from the SOAP request.
        """
        json_to_base64_data = json_to_base64(local_dataset_metadata_path)
        csv_to_base64_data = csv_to_base64(local_dataset_path)
        insights_external_data_id = self.__metadata_writer(dataset_alias=dataset_alias, 
                                                         crma_app_name=crma_app_alias, 
                                                         upload_operation_type=data_operation_type,
                                                         data=json_to_base64_data
                                                         )
        self.__data_writer(insights_external_data_id=insights_external_data_id, data=csv_to_base64_data)
        val = self.__build_csv(insights_external_data_id=insights_external_data_id)
        return val
