import requests
import xml.etree.ElementTree as ET

def login(username: str, password: str, security_token: str) -> tuple:
    """
    Log in to Salesforce and retrieve session ID and server URL.

    Parameters:
    - username (str): Salesforce username.
    - password (str): Salesforce password.
    - security_token (str): Salesforce security token.

    Returns:
    - tuple: A tuple containing session ID and server URL.
    """
    soap_login_url = "https://login.salesforce.com/services/Soap/u/59.0"
    soap_login_header = {
        'content-type': 'text/xml',
        'charset': 'UTF-8',
        'SOAPAction': '""'
    }
    soap_login_request = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:partner.soap.sforce.com">
                                <soapenv:Body>
                                    <urn:login>
                                        <urn:username>{username}</urn:username>
                                        <urn:password>{password}{security_token}</urn:password>
                                    </urn:login>
                                </soapenv:Body>
                            </soapenv:Envelope>"""

    try:
        response = requests.post(url=soap_login_url, data=soap_login_request, headers=soap_login_header)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.RequestException as e:
        print(f'Error during login request: {e}')
        return None, None

    xml_root = ET.fromstring(response.content)
    session_id = xml_root.find('.//{urn:partner.soap.sforce.com}sessionId').text
    server_url = xml_root.find('.//{urn:partner.soap.sforce.com}serverUrl').text
    return session_id, server_url