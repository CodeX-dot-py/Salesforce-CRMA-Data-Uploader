import json
import base64

def json_to_base64(json_file_path: str) -> str:
    """
    Convert JSON data from a file to base64 encoding.

    Parameters:
    - json_file_path (str): Path to the JSON file.

    Returns:
    - str: Base64-encoded string.
    """
    with open(json_file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    datastr = json.dumps(data)
    base64_encoded = base64.b64encode(datastr.encode('utf-8')).decode('utf-8')
    return base64_encoded

def csv_to_base64(csv_file_path: str) -> str:
    """
    Convert CSV data from a file to base64 encoding.

    Parameters:
    - csv_file_path (str): Path to the CSV file.

    Returns:
    - str: Base64-encoded string.
    """
    with open(csv_file_path, 'r') as file:
        csv_data = file.read()
    csv_bytes = csv_data.encode('utf-8')
    base64_encoded = base64.b64encode(csv_bytes).decode('utf-8')
    return base64_encoded
