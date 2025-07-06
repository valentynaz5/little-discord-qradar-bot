from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
QRADAR_API_URL = os.getenv('QRADAR_API_URL')
QRADAR_API_TOKEN = os.getenv('QRADAR_API_TOKEN')
JSON_FILE_PATH = os.getenv('JSON_FILE_PATH')
QRADAR_HOST = os.getenv('QRADAR_HOST')
SEC_TOKEN = os.getenv('SEC_TOKEN')