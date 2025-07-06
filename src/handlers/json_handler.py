import json
import datetime
import os
from config import JSON_FILE_PATH

def init_json_file():
    with open(JSON_FILE_PATH, 'w') as f:
        json.dump([], f, indent=4)

def save_to_json(username, choice):
    if not os.path.exists(JSON_FILE_PATH):
        init_json_file()
    
    with open(JSON_FILE_PATH, 'r') as f:
        data = json.load(f)
    
    entry = {
        'username': username,
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'choice': choice
    }
    data.append(entry)
    
    with open(JSON_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)








