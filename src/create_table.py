import requests
import urllib3
from config import QRADAR_HOST, SEC_TOKEN

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TABLE_NAME = 'discord_bot'
ELEMENT_TYPE = 'ALN'

headers = {
    'SEC': SEC_TOKEN,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

payload = {
    "key_name_types": {
        "username": "ALN",
        "timestamp": "ALN",
        "action": "ALN"
    }
}

url = f"{QRADAR_HOST}/api/reference_data/tables?name={TABLE_NAME}&element_type={ELEMENT_TYPE}"

response = requests.post(url, headers=headers, json=payload, verify=False)

if response.status_code == 201:
    print(f"Reference Table '{TABLE_NAME}' successfully created.")
elif response.status_code == 409:
    print(f"Reference Table '{TABLE_NAME}' already exists.")
else:
    print(f"Failed to create table: {response.status_code} {response.text}")
