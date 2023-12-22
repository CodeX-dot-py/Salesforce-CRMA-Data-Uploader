import json
import base64

def json_to_base64(json_file_path):
    with open(json_file_path) as jsonfile:
        data = json.load(jsonfile)
    datastr = json.dumps(data)
    base64_encoded = base64.b64encode(datastr.encode('utf-8')).decode('utf-8')
    return base64_encoded

def csv_to_base64(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_data = file.read()
    csv_bytes = csv_data.encode('utf-8')
    base64_encoded = base64.b64encode(csv_bytes).decode('utf-8')
    return base64_encoded