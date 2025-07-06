import requests
import urllib3
import json
import urllib.parse
from datetime import datetime
from config import QRADAR_HOST, SEC_TOKEN

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TABLE_NAME = 'discord_bot'

HEADERS = {
    'SEC': SEC_TOKEN,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

def send_to_qradar_table(username, action):
    timestamp = datetime.utcnow().isoformat() + 'Z'

    outer_key = username
    inner_key = timestamp

    value = {
        "username": username,
        "timestamp": timestamp,
        "action": action
    }

    value_param = urllib.parse.quote(json.dumps(value))

    url = f"{QRADAR_HOST}/api/reference_data/tables/{TABLE_NAME}?outer_key={outer_key}&inner_key={inner_key}&value={value_param}"

    try:
        response = requests.post(url, headers=HEADERS, json={}, verify=False)
        if response.status_code == 200:
            print(f"Data successfully added to QRadar table for user: {username}, action: {action}")
        else:
            print(f"Failed to add data to QRadar table: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Error connecting to QRadar: {e}")

        